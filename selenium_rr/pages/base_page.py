import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium_rr.data.urls import Url


class BasePage:
    timeout = 5
    url = Url.BASE_URL

    def __init__(self, browser):
        self.browser = browser

    def all_elements_are_visible(self, locator):
        """this method is used to wait until all elements are visible so that driver is able to interact with them"""
        return WebDriverWait(self.browser, self.timeout).until(EC.visibility_of_all_elements_located(locator))

    def click_on_element(self, locator):
        """this method is used to wait until an element is clickable and then click on it"""
        self.element_is_clickable(locator).click()

    def element_is_clickable(self, locator):
        """this method is used to wait until an element is clickable so that driver is able to interact with it"""
        return WebDriverWait(self.browser, self.timeout).until(EC.element_to_be_clickable(locator))

    def element_is_visible(self, locator):
        """this method is used to wait until an element is visible so that driver is able to interact with it"""
        return WebDriverWait(self.browser, self.timeout).until(EC.visibility_of_element_located(locator))

    def get_length(self, locator):
        """this method is used to get length of a collection of elements"""
        return len(self.browser.find_elements(*locator))

    def get_text(self, locator):
        """this method is used to get text from an element"""
        return self.element_is_visible(locator).text

    @allure.step("open a page")
    def open(self, url=url):
        """this method is used to open a page"""
        self.browser.get(url)
