import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from lesson3.extra_task.locators.checkbox_page_locators import CheckboxPageLocators
from lesson3.extra_task.pages.base_page import BasePage
from lesson3.extra_task.urls import Url


class CheckboxPage(BasePage):
    timeout = 10
    locators = CheckboxPageLocators()

    def __init__(self, browser):
        super().__init__(browser)
        self.url = Url.CHECKBOX_PAGE_URL

    @allure.step("Check if the box is checked")
    def is_box_checked(self, locator):
        """this method is used to check if the box is already checked"""
        checkbox = WebDriverWait(self.browser, self.timeout).until(EC.visibility_of_element_located(locator))
        return checkbox.is_selected()

    @allure.step("Check a chosen checkbox condition")
    def check_checkbox_condition(self, num: int):
        """this method is used to check condition of the chosen checkbox on the page. 
        :num: is a number of the checkbox to check
        
        """
        return self.is_box_checked(self.locators.FIRST_CHECKBOX) if num == 1 else \
            self.is_box_checked(self.locators.SECOND_CHECKBOX)

    @allure.step("Check the box")
    def check_the_box(self, num: int):
        """this method is used to check the box.
        :num: is a number of the checkbox to select

        """
        if num == 1:
            WebDriverWait(self.browser, self.timeout) \
                .until(EC.element_to_be_clickable(self.locators.FIRST_CHECKBOX)).click()
        else:
            WebDriverWait(self.browser, self.timeout) \
                .until(EC.element_to_be_clickable(self.locators.SECOND_CHECKBOX)).click()
        return self
