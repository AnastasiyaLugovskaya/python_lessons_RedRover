import allure

from luma.locators.home_page_locators import HomePageLocators
from luma.locators.whats_new_page_locators import WhatsNewPageLocators
from luma.pages.home_page import HomePage
from luma.pages.whats_new_page import WhatsNewPage


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

    @allure.title("Check redirection to What's New page by clicking a link")
    def test_redirection_to_whats_new_page(self, browser_management):
        with allure.step("Open home page"):
            page = HomePage(browser_management, HomePageLocators.HOME_PAGE_URL)
            page.visit()
        with allure.step("Find What's New link in  the menu"):
            link = page.find_whats_new_link()
        with allure.step("Click on What's New link"):
            link.click()
        page = WhatsNewPage(browser_management, WhatsNewPageLocators.WHATS_NEW_URL)
        with allure.step("Assert current url == What's New Page url"):
            actual_url = page.check_current_url()
            expected_url = WhatsNewPageLocators.WHATS_NEW_URL
            assert actual_url == expected_url, "Urls don't match!" \
                                               f"Expected {expected_url}, got {actual_url}"
        with allure.step("Find header"):
            header = page.is_header_present()
        with allure.step("Assert header contains text \'What's New\'"):
            assert page.is_element_text_correct(header, "What's New"), "There's wrong text in the header"
