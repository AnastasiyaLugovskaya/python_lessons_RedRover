from selenium_rr.locators.header_menu_locators import HeaderMenuLocators
from selenium_rr.pages.base_page import BasePage


class HeaderMenu(BasePage):
    header_locators = HeaderMenuLocators()

    def __init__(self, browser, url):
        super().__init__(browser, url)

    def go_to_basket(self):
        """this method is used to move to basket page"""
        self.element_is_clickable(self.header_locators.BASKET_LINK).click()

    def check_basket_badge_presence(self):
        """this method is used to check if there is a badge with numbers of added goods on the basket"""
        return len(self.all_elements_are_visible(self.header_locators.BASKET_BADGES))

    def get_badge_value(self):
        """this method is used to get a number of added goods from a basket badge"""
        return self.get_text(self.header_locators.BASKET_BADGE)
