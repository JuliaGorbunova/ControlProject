from pages.base import WebPage
from pages.elements import WebElement

class AccountPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://www.onlinetrade.ru/member/'
        super().__init__(web_driver, url)

    email=WebElement(xpath='//span[@class="userInfo__itemData"]')
    error=WebElement(xpath='//p[@text="Указан неверный e-mail или пароль"]')
