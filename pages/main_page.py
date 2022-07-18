import os,pickle

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements
import json
from urllib.parse import urlparse

class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.onlinetrade.ru/'

        super().__init__(web_driver, url)

        # with open('cookies.tmp', 'rb') as cookiesfile:
        #     cookies = pickle.load(cookiesfile)
        # for cookie in cookies:
        #     web_driver.add_cookie(cookie)
        # web_driver.refresh()

    how_to_pay=WebElement(xpath='//a[@title="Как купить"]')
    club_bonus=WebElement(xpath='//a[@title="Клуб ON-бонус"]')
    help=WebElement(xpath='//a[@title="Помощь"]')
    warranty=WebElement(xpath='//a[@title="Гарантия"]')
    points_of_issue=WebElement(xpath='//a[@title="Пункты выдачи"]')
    for_business=WebElement(xpath='//a[@title="ОНЛАЙН ТРЕЙД.РУ для бизнеса"]')
    main_logo=WebElement(id='logo')
    catalog=WebElement(xpath='//a[@title="Каталог товаров"]')
    discounts=WebElement(xpath='//a[@title="Скидки"]')
    search_field=WebElement(xpath='//input[@class="header__search__inputText js__header__search__inputText"]')
    search_button=WebElement(xpath='//input[@class="header__search__inputGogogo"]')
    products_titles=ManyWebElements(xpath='//a[@class="indexGoods__item__name"]')
    auth_button=WebElement(xpath='//a[@title="Вход в Личный кабинет"]')
    bookmarks=WebElement(xpath='//a[@href="/bookmarks.html"]')
    basket=WebElement(xpath='//a[@href="/basket.html"]')
    all_promotions=WebElement(xpath='//a[@href="/actions/"]')
    categoty_menu=WebElement(xpath='//div[@class="catalogLine__panel__left"]')
    auth_form=WebElement(id='popup_login')
    email_field = WebElement(id='ajax_login_popup_email')
    pass_field = WebElement(id='ajax_login_popup_pass')
    login_button=WebElement(xpath='//input[@value="Вход"]')
    all_brands=WebElement(xpath='//a[@href="/brands/"]')
    all_news=WebElement(xpath='//a[@href="/news/"]')















