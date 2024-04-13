import pytest

from selenium_rr.data.user_data import UserData
from selenium_rr.pages.basket_page import BasketPage
from selenium_rr.pages.catalogue_page import CataloguePage
from selenium_rr.pages.checkout_page import CheckoutOverviewPage
from selenium_rr.pages.login_page import LoginPage
from selenium_rr.pages.order_page import OrderPage


class TestOrder:
    order_inv_data = UserData.ORDER_INVALID_DATA
    order_valid_data = UserData.ORDER_VALID_DATA

    @pytest.mark.parametrize("order_values", order_inv_data)
    def test_order_with_invalid_data(self, browser, order_values):
        page = LoginPage(browser)
        page.open()
        page.login_with_valid_data()
        page = CataloguePage(browser)
        page.add_good_to_basket_from_catalogue()
        page.go_to_basket()
        page = BasketPage(browser)
        page.click_on_checkout_button()
        page = OrderPage(browser)
        page.fill_order_fields(order_values[0], order_values[1], order_values[2])
        page.click_on_continue_button()
        assert page.check_error_presence() > 0, "There's no error message!"
        actual_error_message = page.get_error_message()
        assert order_values[3] == actual_error_message, \
            f"There's a wrong message: expected message is {order_values[3]}, " \
            f"actual message is {actual_error_message}"

    def test_order_with_valid_data(self, browser):
        page = LoginPage(browser)
        page.open()
        page.login_with_valid_data()
        page = CataloguePage(browser)
        page.add_good_to_basket_from_catalogue()
        page.go_to_basket()
        page = BasketPage(browser)
        page.click_on_checkout_button()
        page = OrderPage(browser)
        page.fill_order_fields(self.order_valid_data[0], self.order_valid_data[1], self.order_valid_data[2])
        assert page.check_error_presence() == 0, "There's an error message, but shouldn't be!"
        page.go_to_checkout_overview()
        page = CheckoutOverviewPage(browser)
        page.finish_order()
        assert page.check_successful_message_presence() > 0, \
            "There's no successful message, but should be!"
        successful_message = page.get_successful_message()
        expected_message = 'Checkout: Complete!'
        assert successful_message == expected_message, \
            f"Messages aren't equal: expected '{expected_message}', have gotten '{successful_message}'"
