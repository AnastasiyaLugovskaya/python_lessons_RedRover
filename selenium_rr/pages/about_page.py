from selenium_rr.data.urls import Url
from selenium_rr.pages.header_menu import HeaderMenu
from selenium_rr.functions import functions


class AboutPage(HeaderMenu):
    url = Url().ABOUT_PAGE_URL

    def __init__(self, browser):
        super().__init__(browser)

    def get_status_code(self):
        response = functions.get_page_response(self.url)
        return response.status_code
