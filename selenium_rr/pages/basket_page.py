import allure

from selenium_rr.data.urls import Url
from selenium_rr.locators.basket_page_locators import BasketPageLocators
from selenium_rr.pages.header_menu import HeaderMenu


class BasketPage(HeaderMenu):
    basket_locators = BasketPageLocators()
    url = Url().BASKET_URL

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("check a number of added goods that is shown on the basket badge")
    def check_numbers_of_added_goods(self):
        """this method is used to get a number of goods added to basket"""
        return len(self.browser.find_elements(*self.basket_locators.GOODS_LIST))

    @allure.step("click on the checkout button to start making an order")
    def click_on_checkout_button(self):
        """this method is used to click on the checkout button to start making an order"""
        self.element_is_clickable(self.basket_locators.CHECKOUT_BUTTON).click()

    @allure.step("remove a good from the basket")
    def remove_good_from_basket(self):
        """this method is used to remove a good from the basket"""
        self.element_is_clickable(self.basket_locators.REMOVE_BUTTON).click()
