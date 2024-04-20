import allure
import requests
from selenium.common import NoSuchElementException
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from lesson3.extra_task.locators.auth_page_locators import AuthPageLocators
from lesson3.extra_task.pages.base_page import BasePage
from lesson3.extra_task.urls import Url


class AuthPage(BasePage):
    timeout = 10
    locator = AuthPageLocators().CONGRAT_TEXT

    def __init__(self, browser):
        super().__init__(browser)
        self.url = Url.AUTH_PAGE_URL

    @allure.step("Open a page with credentials in url")
    def pass_auth_data_in_url(self):
        self.browser.get(Url.BASE_PAGE_URL_WITH_AUTH_DATA)
        return self

    @allure.step("Get congratulation text")
    def get_congratulation_text(self):
        text = None
        try:
            text = WebDriverWait(self.browser, self.timeout).until(
                EC.visibility_of_element_located(self.locator)).text
        except (NoSuchElementException, TimeoutException):
            text = None
        finally:
            return text

    @allure.step("Base auth by executing http-request")
    def base_auth(self, username, password):
        """this method is used for executing http-request with base authentication"""
        response = self.get_response(username, password)
        page_source = response.text
        self.browser.get("data:text/html;charset=utf-8," + page_source)
        return self

    @allure.step("Get server response")
    def get_response(self, username, password):
        """this method is used to get response from a server"""
        session = requests.Session()
        session.auth = (username, password)
        response = session.get(Url.AUTH_PAGE_URL)
        return response

    @allure.step("Get status code")
    def get_status_code(self, response: requests.Response):
        """this method is used to get a status code from the server response"""
        return response.status_code
