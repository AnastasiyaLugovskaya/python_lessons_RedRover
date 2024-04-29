from selene import browser
from selene.support.shared.jquery_style import s
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 3, 0.5)

    def open_url(self, url):
        s.open(url)

    def find_element(self, selector):
        return s(selector)

    def check_current_url(self):
        return browser.driver.current_url
