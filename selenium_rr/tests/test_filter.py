from selenium_rr.data.urls import Url
from selenium_rr.functions import functions
from selenium_rr.pages.catalogue_page import CataloguePage
from selenium_rr.pages.login_page import LoginPage


class TestFilter:
    url = Url()

    def test_filter_a_to_z(self, browser):
        page = LoginPage(browser, self.url.BASE_URL)
        page.open()
        page.login_with_valid_data()
        page = CataloguePage(browser, self.url.CATALOGUE_URL)
        page.open_filter_menu()
        page.filter_a_to_z()
        goods_list = functions.get_names_of_goods(page.get_goods_list())
        target_list = functions.sort_list(goods_list, reverse_option=False)
        assert target_list == goods_list, \
            "Items aren't sorted according to filter option"

    def test_filter_z_to_a(self, browser):
        page = LoginPage(browser, self.url.BASE_URL)
        page.open()
        page.login_with_valid_data()
        page = CataloguePage(browser, self.url.CATALOGUE_URL)
        page.open_filter_menu()
        page.filter_z_to_a()
        names_list = functions.get_names_of_goods(page.get_goods_list())
        target_list = functions.sort_list(names_list, reverse_option=True)
        assert target_list == names_list, \
            "Items aren't sorted according to filter option"

    def test_filter_hi_to_low(self, browser):
        page = LoginPage(browser, self.url.BASE_URL)
        page.open()
        page.login_with_valid_data()
        page = CataloguePage(browser, self.url.CATALOGUE_URL)
        page.open_filter_menu()
        page.filter_hi_to_low()
        prices_list = functions.get_prices_of_goods(page.get_prices_list())
        target_list = functions.sort_list(prices_list, reverse_option=True)
        assert target_list == prices_list, \
            "Items aren't sorted according to filter option"

    def test_filter_low_to_hi(self, browser):
        page = LoginPage(browser, self.url.BASE_URL)
        page.open()
        page.login_with_valid_data()
        page = CataloguePage(browser, self.url.CATALOGUE_URL)
        page.open_filter_menu()
        page.filter_low_to_hi()
        prices_list = functions.get_prices_of_goods(page.get_prices_list())
        target_list = functions.sort_list(prices_list, reverse_option=False)
        assert target_list == prices_list, \
            "Items aren't sorted according to filter option"
