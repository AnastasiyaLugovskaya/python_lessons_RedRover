from selenium_rr.locators.catalogue_page_locators import CataloguePageLocators
from selenium_rr.pages.base_page import BasePage


class CataloguePage(BasePage):
    catalogue_page_locators = CataloguePageLocators()

    def __init__(self, browser, url):
        super().__init__(browser, url)

    def add_good_to_basket_from_catalogue(self):
        """this method is used to add the first good on the catalogue page to basket"""
        self.element_is_clickable(self.catalogue_page_locators.ADD_TO_BASKET_BUTTON).click()

    def go_to_good_page(self):
        """this method is used to move to the page of the first good in the catalogue"""
        self.element_is_clickable(self.catalogue_page_locators.GOOD_TITLE).click()
