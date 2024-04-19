import allure

from lesson3.extra_task.urls import Url


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.url = Url.BASE_PAGE_URL

    @allure.step("Open a page")
    def open(self):
        """this method is used to open a page"""
        self.browser.get(self.url)
        return self
