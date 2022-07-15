# python -m pytest -v --driver Chrome --driver-path C:\Users\Юлия\PycharmProjects\SmartPageObject\chromedriver.exe tests\test_auth_page.py
from pages.auth_page import AuthPage
import pickle


def test_authorisation(web_browser):

    page = AuthPage(web_browser)
    page.email.send_keys('svy-yuliana@yandex.ru')
    page.password.send_keys('7Fevrala7')
    page.btn.click()

    # Save cookies of the browser after the login
    with open('cookies.tmp', 'wb') as cookies:
        pickle.dump(web_browser.get_cookies(), cookies)

    assert '/all_pets' in page.get_current_url()