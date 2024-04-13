from selenium.common import NoSuchElementException

from .base_page import BasePage
from selenium_rr.locators.auth_page_locators import AuthorizationPageLocators
from selenium_rr.data.user_data import UserData
import random

from ..data.urls import Url


class LoginPage(BasePage):
    auth_locators = AuthorizationPageLocators()
    user_data = UserData()
    url = Url().BASE_URL

    def __init__(self, browser):
        super().__init__(browser)

    def login_with_valid_data(self):
        """this method is used to log in with valid credentials"""
        self.element_is_visible(self.auth_locators.USERNAME_FIELD).send_keys(
            random.choice(self.user_data.ACCEPTED_USERNAMES)
        )
        self.element_is_visible(self.auth_locators.PASSWORD_FIELD).send_keys(self.user_data.PASSWORD)
        self.element_is_clickable(self.auth_locators.LOGIN_BUTTON).click()

    def login_with_invalid_data(self):
        """this method is used to attempt to log in with invalid credentials"""
        self.element_is_visible(self.auth_locators.USERNAME_FIELD).send_keys(self.user_data.INVALID_USERNAME)
        self.element_is_visible(self.auth_locators.PASSWORD_FIELD).send_keys(self.user_data.INVALID_PASSWORD)
        self.element_is_clickable(self.auth_locators.LOGIN_BUTTON).click()

    def get_error_message(self):
        """this method is used for getting an error message during attempting log in with invalid credentials"""
        try:
            error_message = self.get_text(self.auth_locators.ERROR_CONTAINER)
        except NoSuchElementException:
            error_message = None
            print('There are no error container')
        return error_message
