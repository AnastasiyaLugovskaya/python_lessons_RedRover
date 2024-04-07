from selenium_rr.locators.basket_page_locators import BasketPageLocators
from selenium_rr.pages.base_page import BasePage


class BasketPage(BasePage):
    basket_locators = BasketPageLocators()

    def __init__(self, browser, url):
        super().__init__(browser, url)

    def check_numbers_of_added_goods(self):
        return len(self.browser.find_elements(*self.basket_locators.GOODS_LIST))

    def remove_good_from_basket(self):
        self.element_is_clickable(self.basket_locators.REMOVE_BUTTON).click()
