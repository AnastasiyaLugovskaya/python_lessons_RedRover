import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium_rr.data.urls import Url
from selenium_rr.locators.catalogue_page_locators import CataloguePageLocators
from selenium_rr.pages.header_menu import HeaderMenu


class CataloguePage(HeaderMenu):
    catalogue_page_locators = CataloguePageLocators()
    url = Url().CATALOGUE_URL

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("add the first good on the catalogue page to basket")
    def add_good_to_basket_from_catalogue(self):
        """this method is used to add the first good on the catalogue page to basket"""
        self.element_is_clickable(self.catalogue_page_locators.ADD_TO_BASKET_BUTTON).click()

    @allure.step("get the name of a good on a good page")
    def get_good_name(self):
        """this method is used to get the name of a good on a good page"""
        return self.get_text(self.catalogue_page_locators.GOOD_TITLE)

    @allure.step("get list of all goods on the page")
    def get_goods_list(self):
        """this method is used to get list of all goods on the page"""
        goods_list = list(self.all_elements_are_visible(self.catalogue_page_locators.ITEM_LIST))
        return goods_list

    @allure.step("get list of good prices on the page in str format")
    def get_prices_list(self):
        """this method is used to get list of good prices on the page in str format"""
        prices_list = list(self.all_elements_are_visible(self.catalogue_page_locators.PRICE_LIST))
        return prices_list

    @allure.step("move to a good page by clicking on the good image")
    def go_to_good_page_through_good_image(self):
        """this method is used to proceed to good page by clicking on a good image"""
        self.element_is_clickable(self.catalogue_page_locators.GOOD_IMAGE).click()

    @allure.step("move to the page of the first good in the catalogue")
    def go_to_good_page_through_title(self):
        """this method is used to move to the page of the first good in the catalogue"""
        self.element_is_clickable(self.catalogue_page_locators.GOOD_TITLE).click()

    @allure.step("open a filter menu")
    def open_filter_menu(self):
        """this method is used to open a filter menu"""
        filter_menu = self.element_is_clickable(self.catalogue_page_locators.FILTER_ICON)
        filter_menu.click()

    @allure.step("choose 'a-z' filter option")
    def filter_a_to_z(self):
        """this method is used to filter goods by name in alphabetic order"""
        az_filter = self.element_is_clickable(self.catalogue_page_locators.AZ_FILTER)
        az_filter.click()

    @allure.step("choose 'low-high' price filter option")
    def filter_low_to_hi(self):
        """this method is used to filter goods by their price in ascendant order"""
        lohi_filter = self.element_is_clickable(self.catalogue_page_locators.LOHI_FILTER)
        lohi_filter.click()

    @allure.step("choose 'high-low' price filter option")
    def filter_hi_to_low(self):
        """this method is used to filter goods by their price in reversed order"""
        hilo_filter = self.element_is_clickable(self.catalogue_page_locators.HILO_FILTER)
        hilo_filter.click()

    @allure.step("choose 'z-a' filter option")
    def filter_z_to_a(self):
        """this method is used to filter goods by name in reversed alphabetic order"""
        za_filter = self.element_is_clickable(self.catalogue_page_locators.ZA_FILTER)
        za_filter.click()
