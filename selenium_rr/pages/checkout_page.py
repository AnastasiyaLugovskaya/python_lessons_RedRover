from selenium.common import TimeoutException, NoSuchElementException

from selenium_rr.data.urls import Url
from selenium_rr.locators.checkout_locators import CheckoutPageLocators
from selenium_rr.pages.header_menu import HeaderMenu


class CheckoutOverviewPage(HeaderMenu):
    url = Url()
    checkout_locators = CheckoutPageLocators()

    def __init__(self, browser):
        super().__init__(browser)

    def check_successful_message_presence(self):
        """this method is used to check successful message presence after completing an order"""
        try:
            return len(self.all_elements_are_visible(self.checkout_locators.SUCCESSFUL_MESSAGE))
        except (TimeoutException, NoSuchElementException):
            return 0

    def finish_order(self):
        """this method is used to complete an order"""
        self.element_is_clickable(self.checkout_locators.FINISH_BUTTON).click()

    def get_successful_message(self):
        """this method is used to get a successful message after completing an order"""
        return self.get_text(self.checkout_locators.SUCCESSFUL_MESSAGE)
