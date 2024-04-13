from selenium_rr.locators.catalogue_page_locators import CataloguePageLocators
from selenium_rr.locators.header_menu_locators import HeaderMenuLocators
from selenium_rr.pages.basket_page import BasketPage
from selenium_rr.pages.catalogue_page import CataloguePage
from selenium_rr.pages.good_page import GoodPage
from selenium_rr.pages.header_menu import HeaderMenu
from selenium_rr.pages.login_page import LoginPage


class TestBasket:
    catalogue_locators = CataloguePageLocators()
    header_locators = HeaderMenuLocators()

    def test_add_good_to_basket_from_catalogue(self, browser):
        page = LoginPage(browser)
        page.open()
        page.login_with_valid_data()
        page = CataloguePage(browser)
        page.add_good_to_basket_from_catalogue()
        header = HeaderMenu(browser)
        if header.check_basket_badge_presence() > 0:
            number_of_added_goods = header.get_badge_value()
            expected_number = '1'
            assert expected_number == number_of_added_goods, \
                "There is a wrong number of added goods on the badge." \
                f"Expected number = {expected_number}, actual number = {number_of_added_goods}"
        else:
            return "There's no badge on the basket, a good wasn't added to basket"

    def test_remove_good_from_basket(self, browser):
        page = LoginPage(browser)
        page.open()
        page.login_with_valid_data()
        page = CataloguePage(browser)
        page.add_good_to_basket_from_catalogue()
        header = HeaderMenu(browser)
        header.go_to_basket()
        basket_page = BasketPage(browser)
        basket_page.remove_good_from_basket()
        goods_list_length = basket_page.check_numbers_of_added_goods()
        assert 0 == goods_list_length, f"There are still a good in the basket, a number of goods = {goods_list_length}"

    def test_add_good_to_basket_from_good_page(self, browser):
        page = LoginPage(browser)
        page.open()
        page.login_with_valid_data()
        page = CataloguePage(browser)
        page.go_to_good_page()
        page = GoodPage(browser)
        page.add_good_to_basket_from_good_page()
        header = HeaderMenu(browser)
        if header.check_basket_badge_presence() > 0:
            number_of_added_goods = header.get_badge_value()
            expected_number = '1'
            assert expected_number == number_of_added_goods, \
                "There is a wrong number of added goods on the badge." \
                f"Expected number = {expected_number}, actual number = {number_of_added_goods}"
        else:
            return "There's no badge on the basket, a good wasn't added to basket"
