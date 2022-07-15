from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://www.onlinetrade.ru/member/login.html'
        super().__init__(web_driver, url)

    email_field = WebElement(xpath='//input[@name="login"]')
    pass_field = WebElement(xpath='//input[@name="password"]')
    login_button=WebElement(xpath='//input[@class="button button__orange"]')
    forget_pass=WebElement(xpath='//a[@title="Забыли пароль?"]')
    reg_button=WebElement(xpath='//a[@title="Зарегистрироваться"]')
    checkbox_remember_me=WebElement(xpath='//span[@class="ui-checkboxradio-icon ui-corner-all ui-icon ui-icon-background ui-state-hover ui-icon-blank"]')




