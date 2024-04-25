from luma.pages.home_page import HomePage
from luma.locators.home_page_locators import HomePageLocators


class TestWhatsNew:
    def test_whats_new_link_visibility(self, browser_management):
        page = HomePage(browser_management, HomePageLocators.HOME_PAGE_URL)
        page.visit()
