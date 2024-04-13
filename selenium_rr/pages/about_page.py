from selenium_rr.pages.header_menu import HeaderMenu
from selenium_rr.functions import functions


class AboutPage(HeaderMenu):

    def __init__(self, browser, url):
        super().__init__(browser, url)

    def get_status_code(self):
        response = functions.check_page_response(self.url)
        return response.status_code
