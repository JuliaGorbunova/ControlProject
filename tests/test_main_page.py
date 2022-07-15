# python -m pytest -v --driver Chrome --driver-path C:\Users\Юлия\PycharmProjects\SmartPageObject\chromedriver.exe tests\test_main_page.py

import pytest
import pickle
from selenium.common import NoSuchElementException
from pages.main_page import MainPage
from selenium import webdriver
from selenium.webdriver import ActionChains

def test_how_to_pay_link(web_browser):
    """при клике на ссылку "Как купить" происходит переход на соответствущую страницу"""
    page = MainPage(web_browser)
    page.how_to_pay.click()
    assert page.get_relative_link()=='info/delivery.html','Ссылка "Как купить" не ведет на соответствующую страницу'

def test_club_bonus_link(web_browser):
    """при клике на ссылку "Клуб ON бонус" происходит переход на соответствущую страницу"""
    page = MainPage(web_browser)
    page.club_bonus.click()
    assert page.get_relative_link()=='club/','Ссылка "Клуб ON бонус" не ведет на соответствующую страницу'

def test_help_link(web_browser):
    """при клике на ссылку "Помощь" происходит переход на соответствущую страницу"""
    page = MainPage(web_browser)
    page.help.click()
    assert page.get_relative_link()=='feedback/','Ссылка "Помощь" не ведет на соответствующую страницу'

def test_warranty_link(web_browser):
    """при клике на ссылку "Гарантии" происходит переход на соответствущую страницу"""
    page = MainPage(web_browser)
    page.warranty.click()
    assert page.get_relative_link()=='info/garantii.html','Ссылка "Гарантии" не ведет на соответствующую страницу'

def test_points_of_issue_link(web_browser):
    """Пункты выдачи"""
    page = MainPage(web_browser)
    page.points_of_issue.click()
    assert page.get_relative_link()=='shops/nizhniy_novgorod/','Ссылка "Пункты выдачи" не ведет на соответствующую страницу'

def test_for_business_link(web_browser):
    """при клике на ссылку "Для бизнеса" происходит переход на соответствущую страницу"""
    page = MainPage(web_browser)
    page.for_business.click()
    assert page.get_relative_link()=='info/beznal.html?utm_source=internal&utm_medium=headlinemenu&utm_campaign=b1','Ссылка "Для бизнеса" не ведет на соответствующую страницу'

def test_logo_link(web_browser):
    """при клике на логотип "ОнлайнТрейд" происходит переход на главную страницу сайта"""
    page = MainPage(web_browser)
    page.main_logo.click()
    assert page.get_current_url() == 'https://www.onlinetrade.ru/','При нажатии на логотип "ОнлайнТрейд" не происходит перехода на главную страницу сайта'

def test_drop_menu_catalog_link(web_browser):
    """при клике на логотип "ОнлайнТрейд" происходит переход на главную страницу сайта"""
    page = MainPage(web_browser)
    page.catalog.click()
    res=page.categoty_menu.find().is_displayed()
    assert res,'Кнопка "Каталог" не вызывает выпадающее меню'

def test_actions_link(web_browser):
    """при нажатии на кнопку "Скидки" происходит переход на страницу со скидками"""
    page = MainPage(web_browser)
    page.discounts.click()
    assert page.get_relative_link() == 'actions/','Нажатие на кнопку "Скидки" не ведет на страницу со скидками'

def test_auth_form_link(web_browser):
    """при клике на кнопку входа происходит переход к форме для ввода логина и пароля"""
    page = MainPage(web_browser)
    page.auth_button.click()
    res=page.auth_form.find().is_displayed()
    assert res,'При нажатии на кнопку авторизации не происходит переход к форме авторизации'

def test_auth_page_link(web_browser):
    """при клике на кнопку входа происходит переход на страницу авторизации"""
    page = MainPage(web_browser)
    page.auth_button.click()
    assert page.get_relative_link() == 'member / login.html', 'При нажатии на кнопку входа правойк кнопкой мыши и выборе' \
                                                              'открытия новой вкладки не происходит переход на страницу авторизации'

def test_bookmarks(web_browser):
    """при клике на логотип "Закладки" происходит переход на страницу с закладками"""
    page = MainPage(web_browser)
    page.bookmarks.click()
    assert page.get_relative_link() == 'bookmarks.html', 'Нажатие на кнопку "Закладки" не ведет на страницу с закладками'

def test_basket(web_browser):
    """при клике на логотип "Корзина" происходит переход на страницу корзины"""
    page = MainPage(web_browser)
    page.basket.click()
    assert page.get_relative_link() == 'basket.html', 'Нажатие на кнопку "Корзина" не ведет на страницу корзины'

def test_all_promotions(web_browser):
    """при клике на ссылку "Все акции" происходит переход на страницу акций"""
    page = MainPage(web_browser)
    page.all_promotions.click()
    assert page.get_relative_link() == 'actions/', 'Клик на ссылку "Все акции" не ведет на страницу акций'

def test_all_brands(web_browser):
    """при клике на ссылку "Все бренды" происходит переход на страницу акций"""
    page = MainPage(web_browser)
    page.all_brands.click()
    assert page.get_relative_link() == 'brands/', 'Клик на ссылку "Все бренды" не ведет на страницу брендов'

def test_all_news(web_browser):
    """при клике на ссылку "Все новости" происходит переход на страницу акций"""
    page = MainPage(web_browser)
    page.all_news.click()
    assert page.get_relative_link() == 'news/', 'Клик на ссылку "Все новости" не ведет на страницу новостей'

def test_auth(web_browser):
    """при вводе в поля формы авторизации корректных данных действующего пользователя происходит вход в аккаунт"""
    page = MainPage(web_browser)
    page.auth_button.click()
    page.email_field.send_keys(correct_login)
    page.pass_field.send_keys(correct_pass)

    assert page.get_relative_link() == 'news/', 'Клик на ссылку "Все новости" не ведет на страницу новостей'
