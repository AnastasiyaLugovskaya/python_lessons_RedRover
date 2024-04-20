import allure
from selenium import webdriver

from lesson3.extra_task.locators.add_page_locators import AddPageLocators
from lesson3.extra_task.pages.base_page import BasePage
from lesson3.extra_task.urls import Url
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddPage(BasePage):
    timeout = 10
    add_page_locators = AddPageLocators()

    def __init__(self, browser: webdriver.Chrome):
        super().__init__(browser)
        self.url = Url.ADD_PAGE_URL

    @allure.step("Click on add button")
    def click_on_add_button(self, number):
        """this method is used to click on add button"""
        for i in range(number):
            WebDriverWait(self.browser, self.timeout)\
                .until(EC.element_to_be_clickable(self.add_page_locators.ADD_ELEMENT_BUTTON)).click()
        return self

    @allure.step("Get number of added elements")
    def get_number_of_added_elements(self):
        """this method is used to get number of added elements"""
        lst = list(WebDriverWait(self.browser, self.timeout)
                   .until(EC.visibility_of_all_elements_located(self.add_page_locators.DELETE_BUTTON)))
        return len(lst)

    @allure.step("Click on delete button")
    def click_on_delete_button(self, number):
        """this method is used to remove elements from the page"""
        for i in range(number):
            WebDriverWait(self.browser, self.timeout)\
                .until(EC.element_to_be_clickable(self.add_page_locators.FIRST_DELETE_BUTTON)).click()
        return self

    @allure.step("Check there are no elements on the page")
    def check_the_page_has_no_elements(self):
        """This method is used to check there are no elements on the page after deleting"""
        return True if len(list(self.browser.find_elements(*self.add_page_locators.DELETE_BUTTON))) == 0 else False
