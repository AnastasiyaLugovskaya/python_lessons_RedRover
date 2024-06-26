import allure

from selenium_rr.locators.header_menu_locators import HeaderMenuLocators
from selenium_rr.pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class HeaderMenu(BasePage):
    header_locators = HeaderMenuLocators()

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("check there's a badge on the basket")
    def check_basket_badge_presence(self):
        """this method is used to check if there is a badge with numbers of added goods on the basket"""
        try:
            return len(self.all_elements_are_visible(self.header_locators.BASKET_BADGES))
        except (TimeoutException, NoSuchElementException):
            return 0

    @allure.step("click on the about link in the burger menu")
    def click_on_about_link(self):
        """this method is used to move to about page"""
        self.click_on_element(self.header_locators.ABOUT_LINK)

    @allure.step("open the burger menu")
    def click_on_burger_menu(self):
        """this method is used to open burger menu"""
        self.click_on_element(self.header_locators.BURGER_MENU)

    @allure.step("click on the reset link in the burger menu")
    def click_on_reset_link(self):
        """this method is used to click on a reset link in order to clear a basket"""
        self.click_on_element(self.header_locators.RESET_LINK)

    @allure.step("get a number from the basket badge")
    def get_badge_value(self):
        """this method is used to get a number of added goods from a basket badge"""
        return self.get_text(self.header_locators.BASKET_BADGE)

    @allure.step("move to the basket page")
    def go_to_basket(self):
        """this method is used to move to basket page"""
        self.element_is_clickable(self.header_locators.BASKET_LINK).click()

    @allure.step("click on the logout link in the  burger menu")
    def logout(self):
        """this method is used to log out of system"""
        logout_link = self.element_is_clickable(self.header_locators.LOGOUT_LINK)
        logout_link.click()
