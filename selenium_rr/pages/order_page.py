from selenium.common import TimeoutException, NoSuchElementException

from selenium_rr.data.urls import Url
from selenium_rr.locators.order_page_locators import OrderPageLocators
from selenium_rr.pages.header_menu import HeaderMenu


class OrderPage(HeaderMenu):
    order_locators = OrderPageLocators()
    url = Url().ORDER_PAGE_URL

    def __init__(self, browser):
        super().__init__(browser)

    def check_error_presence(self):
        """this method is used to check presence of error message after attempting to make an order without
        filling out all required fields"""

        try:
            return len(self.all_elements_are_visible(self.order_locators.ERROR_MESSAGE))
        except (TimeoutException, NoSuchElementException):
            return 0

    def click_on_continue_button(self):
        """this method is used to click on continue button on the order page"""
        self.element_is_clickable(self.order_locators.CONTINUE_BUTTON).click()

    def fill_order_fields(self, first_name, last_name, code):
        """this method is used to fill order fields with sent data"""
        self.element_is_visible(self.order_locators.FIRSTNAME_FIELD).send_keys(first_name)
        self.element_is_visible(self.order_locators.LASTNAME_FIELD).send_keys(last_name)
        self.element_is_visible(self.order_locators.POSTAL_CODE_FIELD).send_keys(code)

    def get_error_message(self):
        """this method is used to get text value from error message"""
        return self.get_text(self.order_locators.ERROR_MESSAGE)

    def go_to_checkout_overview(self):
        """this method is used to proceed to 2nd step of performing an order"""
        self.click_on_continue_button()
