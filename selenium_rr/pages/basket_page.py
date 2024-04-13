from selenium_rr.data.urls import Url
from selenium_rr.locators.basket_page_locators import BasketPageLocators
from selenium_rr.pages.header_menu import HeaderMenu


class BasketPage(HeaderMenu):
    basket_locators = BasketPageLocators()
    url = Url().BASKET_URL

    def __init__(self, browser):
        super().__init__(browser)

    def check_numbers_of_added_goods(self):
        return len(self.browser.find_elements(*self.basket_locators.GOODS_LIST))

    def click_on_checkout_button(self):
        self.element_is_clickable(self.basket_locators.CHECKOUT_BUTTON).click()

    def remove_good_from_basket(self):
        self.element_is_clickable(self.basket_locators.REMOVE_BUTTON).click()
