# python -m pytest -v --driver Chrome --driver-path C:\Users\Юлия\PycharmProjects\SmartPageObject\chromedriver.exe tests\test_auth_page.py
from pages.auth_page import AuthPage
from pages.account_page import AccountPage
from data import correct_email,correct_pass,incorrect_email,incorrect_pass

def test_authorisation_with_correct_data(web_browser):
    """при вводе в поля формы авторизации корректных данных действующего пользователя происходит вход в аккаунт"""
    page = AuthPage(web_browser)
    page.email_field.send_keys(correct_email)
    page.pass_field.send_keys(correct_pass)
    page.login_button.click()
    page = AccountPage(web_browser)
    res = (page.email.find().is_displayed()) and (
                ('Клиентский номер, ID:') in page.get_page_source()), 'При вводе в поля формы авторизации' \
                                                                      ' корректных данных действующего пользователя ' \
                                                                      'не происходит вход в аккаунт'

    def test_auth_with_uncorrect_email(web_browser):
        """при вводе в поля формы авторизации некорректного email происходит переход на страницу с сообщением об ошибке"""
        page = AuthPage(web_browser)
        page.email_field.send_keys(incorrect_email)
        page.pass_field.send_keys(correct_pass)
        page.login_button.click()
        assert 'Указан неверный e-mail или пароль' in page.get_page_source()

    def test_auth_with_uncorrect_pass(web_browser):
        """при вводе в поля формы авторизации некорректного пароля появляется сообщение об ошибке"""
        page = AuthPage(web_browser)
        page.email_field.send_keys(correct_email)
        page.pass_field.send_keys(incorrect_pass)
        page.login_button.click()
        assert 'Указан неверный e-mail или пароль' in page.get_page_source()

    # # Save cookies of the browser after the login
    # with open('cookies.tmp', 'wb') as cookies:
    #     pickle.dump(web_browser.get_cookies(), cookies)




