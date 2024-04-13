import pytest

from selenium_rr.data.urls import Url
from selenium_rr.pages.about_page import AboutPage
from selenium_rr.pages.basket_page import BasketPage
from selenium_rr.pages.catalogue_page import CataloguePage
from selenium_rr.pages.login_page import LoginPage


class TestBurgerMenu:
    url = Url()

    def test_logout(self, browser):
        target_url = self.url.BASE_URL
        page = LoginPage(browser, self.url.BASE_URL)
        page.open()
        page.login_with_valid_data()
        page = CataloguePage(browser, self.url.CATALOGUE_URL)
        page.click_on_burger_menu()
        page.logout()
        current_url = browser.current_url
        assert target_url == current_url, \
            f"URLs don't match, user didn't log out. Expected url is '{target_url}', current url is '{current_url}'"

    @pytest.mark.xfail
    def test_about_button(self, browser):
        page = LoginPage(browser, self.url.BASE_URL)
        page.open()
        page.login_with_valid_data()
        page = CataloguePage(browser, self.url.CATALOGUE_URL)
        page.click_on_burger_menu()
        page.click_on_about_link()
        page = AboutPage(browser, self.url.ABOUT_PAGE_URL)
        actual_response = page.get_status_code()
        expected_response = 200
        assert actual_response == expected_response, \
            f"Status code is {actual_response}, expected code is {expected_response}."

    def test_reset_app_state(self, browser):
        page = LoginPage(browser, self.url.BASE_URL)
        page.open()
        page.login_with_valid_data()
        page = CataloguePage(browser, self.url.CATALOGUE_URL)
        page.add_good_to_basket_from_catalogue()
        page.click_on_burger_menu()
        page.click_on_reset_link()
        actual_badge = page.check_basket_badge_presence()
        expected_badge = 0
        page.go_to_basket()
        page = BasketPage(browser, self.url.BASKET_URL)
        actual_number_of_goods = page.check_numbers_of_added_goods()
        expected_number_of_goods = 0
        assert expected_badge == actual_badge and expected_number_of_goods == actual_number_of_goods, \
            f"Reset link didn't work. Expected number on the badge is {expected_badge}, "\
            f"actual number is {actual_badge}" \
            f"Expected number of goods in the basket is {expected_number_of_goods}, actual number is " \
            f"{actual_number_of_goods}"
