from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium_rr.data.urls import Url


class BasePage:
    timeout = 5
    url = Url.BASE_URL

    def __init__(self, browser):
        self.browser = browser

    def all_elements_are_visible(self, locator):
        return WebDriverWait(self.browser, self.timeout).until(EC.visibility_of_all_elements_located(locator))

    def click_on_element(self, locator):
        self.element_is_clickable(locator).click()

    def element_is_clickable(self, locator):
        return WebDriverWait(self.browser, self.timeout).until(EC.element_to_be_clickable(locator))

    def element_is_visible(self, locator):
        return WebDriverWait(self.browser, self.timeout).until(EC.visibility_of_element_located(locator))

    def get_length(self, locator):
        return len(self.browser.find_elements(*locator))

    def get_text(self, locator):
        return self.element_is_visible(locator).text

    def open(self, url=url):
        self.browser.get(url)
