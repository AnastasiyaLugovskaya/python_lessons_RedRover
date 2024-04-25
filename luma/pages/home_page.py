from selenium.webdriver.chrome.webdriver import WebDriver

from luma.pages.base_page import BasePage
from selene import browser, by, be, have
from selene.support.shared.jquery_style import s, ss
from luma.locators.home_page_locators import HomePageLocators


class HomePage(BasePage):

    def find_menu(self):
        return s(HomePageLocators.HOME_PAGE_MENU)

    def visit(self):
        browser.open(self.url)
