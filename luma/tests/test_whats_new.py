import allure

from luma.pages.home_page import HomePage
from luma.locators.home_page_locators import HomePageLocators


@allure.suite("Testing What's New Page")
class TestWhatsNew:
    @allure.title("Test visibility of What's New link on the home page")
    def test_whats_new_link_visibility(self, browser_management):
        with allure.step("Open home page"):
            page = HomePage(browser_management, HomePageLocators.HOME_PAGE_URL)
            page.visit()
        with allure.step("Assert home page menu presence"):
            assert page.is_menu_present(), "There's no  menu on the page"
        with allure.step("Assert there is the What's New link in the menu"):
            assert page.is_whats_new_link_present(), "there's no What's new link in the menu"

