from .base_page import BasePage
from selenium_rr.locators.auth_page_locators import AuthorizationPage
from selenium_rr.data.user_data import UserData
import random


class LoginPage(BasePage):
    auth_locators = AuthorizationPage()
    user_data = UserData()

    def __init__(self, browser, url):
        super().__init__(browser, url)

    def login_with_valid_data(self):
        self.element_is_visible(self.auth_locators.USERNAME_FIELD).send_keys(
            random.choice(self.user_data.ACCEPTED_USERNAMES)
        )
        self.element_is_visible(self.auth_locators.PASSWORD_FIELD).send_keys(self.user_data.PASSWORD)
        self.element_is_clickable(self.auth_locators.LOGIN_BUTTON).click()

    def login_with_invalid_data(self):
        self.element_is_visible(self.auth_locators.USERNAME_FIELD).send_keys(self.user_data.INVALID_USERNAME)
        self.element_is_visible(self.auth_locators.PASSWORD_FIELD).send_keys(self.user_data.INVALID_PASSWORD)
        self.element_is_clickable(self.auth_locators.LOGIN_BUTTON).click()
