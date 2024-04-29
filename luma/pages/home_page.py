from selenium.webdriver.chrome.webdriver import WebDriver

from luma.pages.base_page import BasePage
from selene import browser, by, be, have
from selene.support.shared.jquery_style import s, ss
from luma.locators.home_page_locators import HomePageLocators


class HomePage(BasePage):
    locators = HomePageLocators()

    def is_whats_new_link_present(self):
        return self.find_element(self.locators.WHATS_NEW_LINK).should(be.present)

    def is_menu_present(self):
        return self.find_element(self.locators.HOME_PAGE_MENU).should(be.present)

    # def find_menu(self):
    #     return s(self.locators.HOME_PAGE_MENU)
    #
    # def find_whats_new_link(self):
    #     return s(self.locators.WHATS_NEW_LINK)

    def visit(self):
        browser.open(self.url)
