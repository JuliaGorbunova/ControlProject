# python -m pytest -v --driver Chrome --driver-path C:\Users\Юлия\PycharmProjects\ControlProject\chromedriver.exe tests\test_main_page.py

from pages.main_page import MainPage
from pages.account_page import AccountPage
from tests.data import correct_email,correct_pass,incorrect_email,incorrect_pass

def test_how_to_pay_link(web_browser):
    """при клике на ссылку "Как купить" происходит переход на соответствущую страницу"""
    page = MainPage(web_browser)
    page.how_to_pay.click()
    assert page.get_relative_link()=='/info/delivery.html','Ссылка "Как купить" не ведет на соответствующую страницу'

def test_club_bonus_link(web_browser):
    """при клике на ссылку "Клуб ON бонус" происходит переход на соответствущую страницу"""
    page = MainPage(web_browser)
    page.club_bonus.click()
    assert page.get_relative_link()=='/club/','Ссылка "Клуб ON бонус" не ведет на соответствующую страницу'

def test_help_link(web_browser):
    """при клике на ссылку "Помощь" происходит переход на соответствущую страницу"""
    page = MainPage(web_browser)
    page.help.click()
    assert page.get_relative_link()=='/feedback/','Ссылка "Помощь" не ведет на соответствующую страницу'

def test_warranty_link(web_browser):
    """при клике на ссылку "Гарантии" происходит переход на соответствущую страницу"""
    page = MainPage(web_browser)
    page.warranty.click()
    assert page.get_relative_link()=='/info/garantii.html','Ссылка "Гарантии" не ведет на соответствующую страницу'

def test_points_of_issue_link(web_browser):
    """Пункты выдачи"""
    page = MainPage(web_browser)
    page.points_of_issue.click()
    assert '/shops/' in page.get_current_url(),'Ссылка "Пункты выдачи" не ведет на соответствующую страницу'

def test_for_business_link(web_browser):
    """при клике на ссылку "Для бизнеса" происходит переход на соответствущую страницу"""
    page = MainPage(web_browser)
    page.for_business.click()
    assert page.get_relative_link()=='/info/beznal.html','Ссылка "Для бизнеса" не ведет на соответствующую страницу'

def test_logo_link(web_browser):
    """при клике на логотип "ОнлайнТрейд" происходит переход на главную страницу сайта"""
    page = MainPage(web_browser)
    page.main_logo.click()
    assert page.get_current_url() == 'https://www.onlinetrade.ru/','При нажатии на логотип "ОнлайнТрейд" не происходит перехода на главную страницу сайта'

def test_drop_menu_catalog_link(web_browser):
    """при клике на кнопку "Каталог" открывается выпадающее меню с видами товаров"""
    page = MainPage(web_browser)
    page.catalog.click()
    res=page.categoty_menu.find().is_displayed()
    assert res,'Кнопка "Каталог" не вызывает выпадающее меню'

def test_actions_link(web_browser):
    """при нажатии на кнопку "Скидки" происходит переход на страницу со скидками"""
    page = MainPage(web_browser)
    page.discounts.click()
    assert page.get_relative_link() == '/actions/','Нажатие на кнопку "Скидки" не ведет на страницу со скидками'

def test_auth_form_link(web_browser):
    """при клике на кнопку входа происходит переход к форме для ввода логина и пароля"""
    page = MainPage(web_browser)
    page.auth_button.click()
    res=page.auth_form.find().is_displayed()
    assert res,'При нажатии на кнопку авторизации не происходит переход к форме авторизации'

def test_bookmarks(web_browser):
    """при клике на логотип "Закладки" происходит переход на страницу с закладками"""
    page = MainPage(web_browser)
    page.bookmarks.click()
    assert page.get_relative_link() == '/bookmarks.html', 'Нажатие на кнопку "Закладки" не ведет на страницу с закладками'

def test_basket(web_browser):
    """при клике на логотип "Корзина" происходит переход на страницу корзины"""
    page = MainPage(web_browser)
    page.basket.click()
    assert page.get_relative_link() == '/basket.html', 'Нажатие на кнопку "Корзина" не ведет на страницу корзины'

def test_all_promotions(web_browser):
    """при клике на ссылку "Все акции" происходит переход на страницу акций"""
    page = MainPage(web_browser)
    page.all_promotions.click()
    assert page.get_relative_link() == '/actions/', 'Клик на ссылку "Все акции" не ведет на страницу акций'

def test_all_brands(web_browser):
    """при клике на ссылку "Все бренды" происходит переход на страницу акций"""
    page = MainPage(web_browser)
    page.all_brands.click()
    assert page.get_relative_link() == '/brands/', 'Клик на ссылку "Все бренды" не ведет на страницу брендов'

def test_all_news(web_browser):
    """при клике на ссылку "Все новости" происходит переход на страницу акций"""
    page = MainPage(web_browser)
    page.all_news.click()
    assert page.get_relative_link() == '/news/', 'Клик на ссылку "Все новости" не ведет на страницу новостей'

def test_auth_with_correct_data(web_browser):
    """при вводе в поля формы авторизации корректных данных действующего пользователя происходит вход в аккаунт"""
    page = MainPage(web_browser)
    page.auth_button.click()
    page.email_field.send_keys(correct_email)
    page.pass_field.send_keys(correct_pass)
    page.login_button.click()
    page=AccountPage(web_browser)
    res=(page.email.find().is_displayed()) and (('Клиентский номер, ID:') in page.get_page_source()),'При вводе в поля формы авторизации' \
                                                                                                     ' корректных данных действующего пользователя ' \
                                                                                                     'не происходит вход в аккаунт'

def test_auth_with_uncorrect_email(web_browser):
    """при вводе в поля формы авторизации некорректного email происходит переход на страницу с сообщением об ошибке"""
    page = MainPage(web_browser)
    page.auth_button.click()
    page.email_field.send_keys(incorrect_email)
    page.pass_field.send_keys(correct_pass)
    page.login_button.click()
    assert 'Указан неверный e-mail или пароль' in page.get_page_source()

def test_auth_with_uncorrect_pass(web_browser):
    """при вводе в поля формы авторизации некорректного пароля появляется сообщение об ошибке"""
    page = MainPage(web_browser)
    page.auth_button.click()
    page.email_field.send_keys(correct_email)
    page.pass_field.send_keys(incorrect_pass)
    page.login_button.click()
    assert 'Указан неверный e-mail или пароль' in page.get_page_source()



