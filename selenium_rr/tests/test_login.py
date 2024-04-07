from selenium.common import NoSuchElementException
from selenium_rr.data.urls import Url
from selenium_rr.pages.login_page import LoginPage
from selenium_rr.locators.auth_page_locators import AuthorizationPage


class TestLogin:
    url = Url()
    auth_locators = AuthorizationPage()

    def test_login_with_valid_data(self, browser):
        target_url = self.url.CATALOGUE_URL
        page = LoginPage(browser, url=self.url.BASE_URL)
        page.open()
        page.login_with_valid_data()
        current_url = browser.current_url
        assert target_url == current_url, \
            f"URLs don't match, user didn't log in. Expected url is '{target_url}', current url is '{current_url}'"

    def test_login_with_invalid_data(self, browser):
        target_message = 'Epic sadface: Username and password do not match any user in this service'
        page = LoginPage(browser, url=self.url.BASE_URL)
        page.open()
        page.login_with_invalid_data()
        try:
            error_message = page.get_text(self.auth_locators.ERROR_CONTAINER)
        except NoSuchElementException:
            error_message = None
            print('There are no error container')
        assert target_message == error_message, \
            f"There's no error message, user logged in but shouldn't. Expected error message is '{target_message}'"\
            f"actual error message is '{error_message}'"

