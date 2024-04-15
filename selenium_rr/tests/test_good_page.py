import allure

from selenium_rr.pages.catalogue_page import CataloguePage
from selenium_rr.pages.good_page import GoodPage
from selenium_rr.pages.header_menu import HeaderMenu
from selenium_rr.pages.login_page import LoginPage


@allure.epic("Testing a good page")
class TestGoodPage:
    @allure.title("Test moving to the first good's page by clicking on its image")
    def test_go_to_good_page_through_image(self, browser):
        page = LoginPage(browser)
        page.open()
        page.login_with_valid_data()
        page = CataloguePage(browser)
        good_name_in_catalogue = page.get_good_name()
        page.go_to_good_page_through_good_image()
        page = GoodPage(browser)
        good_name_on_good_page = page.get_good_name()
        assert good_name_on_good_page == good_name_in_catalogue, \
            f"The good name and expected name don't match, there is a wrong page opened. " \
            f"Expected good name is '{good_name_in_catalogue}', actual good name is '{good_name_on_good_page}'"

    @allure.title("Test moving to the first good's page by clicking on its title")
    def test_go_to_good_page_through_title(self, browser):
        page = LoginPage(browser)
        page.open()
        page.login_with_valid_data()
        page = CataloguePage(browser)
        good_name_in_catalogue = page.get_good_name()
        page.go_to_good_page_through_title()
        page = GoodPage(browser)
        good_name_on_good_page = page.get_good_name()
        assert good_name_on_good_page == good_name_in_catalogue, \
            f"The good name and expected name don't match, there is a wrong page opened. " \
            f"Expected good name is '{good_name_in_catalogue}', actual good name is '{good_name_on_good_page}'"

    @allure.title("Test removing a good from the basket by clicking on 'Remove' button on the good's page")
    def test_remove_good_from_good_page(self, browser):
        page = LoginPage(browser)
        page.open()
        page.login_with_valid_data()
        page = CataloguePage(browser)
        page.add_good_to_basket_from_catalogue()
        page.go_to_good_page_through_title()
        page = GoodPage(browser)
        page.remove_good_from_basket_from_good_page()
        header = HeaderMenu(browser)
        badge = header.check_basket_badge_presence()
        assert badge == 0, "There is still be a badge on the basket, a good wasn't removed"\
            f"Expected number in the badge = 0, actual number in the badge = {badge}"
