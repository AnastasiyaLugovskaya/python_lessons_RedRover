from selenium_rr.data.urls import Url
from selenium_rr.pages.catalogue_page import CataloguePage
from selenium_rr.pages.login_page import LoginPage


class TestBurgerMenu:
    url = Url()

    def test_logout(self, browser):
        target_url = self.url.BASE_URL
        page = LoginPage(browser, self.url.BASE_URL)
        page.open()
        page.login_with_valid_data()
        page = CataloguePage(browser, self.url.CATALOGUE_URL)
        page.click_on_burger_menu()
        page.logout()
        current_url = browser.current_url
        assert target_url == current_url, \
            f"URLs don't match, user didn't log out. Expected url is '{target_url}', current url is '{current_url}'"
