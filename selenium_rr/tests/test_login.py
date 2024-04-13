from selenium_rr.data.urls import Url
from selenium_rr.pages.login_page import LoginPage
from selenium_rr.locators.auth_page_locators import AuthorizationPageLocators


class TestLogin:
    url = Url()
    auth_locators = AuthorizationPageLocators()

    def test_login_with_valid_data(self, browser):
        target_url = self.url.CATALOGUE_URL
        page = LoginPage(browser)
        page.open()
        page.login_with_valid_data()
        current_url = browser.current_url
        assert target_url == current_url, \
            f"URLs don't match, user didn't log in. Expected url is '{target_url}', current url is '{current_url}'"

    def test_login_with_invalid_data(self, browser):
        target_message = 'Epic sadface: Username and password do not match any user in this service'
        page = LoginPage(browser)
        page.open()
        page.login_with_invalid_data()
        error_message = page.get_error_message()
        assert target_message == error_message, \
            f"There's no error message, user logged in but shouldn't. Expected error message is '{target_message}'"\
            f"actual error message is '{error_message}'"
