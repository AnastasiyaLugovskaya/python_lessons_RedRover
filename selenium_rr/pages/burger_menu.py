from selenium_rr.pages.header_menu import HeaderMenu


class BurgerMenu(HeaderMenu):
    def __init__(self, browser, url):
        super().__init__(browser, url)
