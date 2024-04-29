from selene.support.shared.jquery_style import s
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver: WebDriver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 10)

    def open_url(self, url):
        s.open(url)

    def find_element(self, selector):
        return s(selector)

    # def open(self):
    #     self.driver.get(self.url)
    #
    # def is_visible(self, locator):
    #     return self.wait.until(ec.visibility_of_element_located(locator))
