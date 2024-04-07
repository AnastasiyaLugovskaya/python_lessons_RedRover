from selenium_rr.locators.good_page_locators import GoodPageLocators
from selenium_rr.pages.header_menu import HeaderMenu


class GoodPage(HeaderMenu):
    good_page_locators = GoodPageLocators()

    def __init__(self, browser, url):
        super().__init__(browser, url)

    def add_good_to_basket_from_good_page(self):
        """this method is used for adding a good to basket from the good page"""
        self.element_is_clickable(self.good_page_locators.ADD_BUTTON).click()

    def remove_good_from_basket_from_good_page(self):
        """this method is used for removing a good from basket from the good page"""
        self.element_is_clickable(self.good_page_locators.REMOVE_BUTTON).click()
