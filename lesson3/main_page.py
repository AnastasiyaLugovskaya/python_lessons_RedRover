import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from lesson3.data.data import Data
from lesson3.data.urls import Url
from lesson3.main_page_locators import MainPageLocators


class MainPage:
    url = Url().MAIN_PAGE_URL
    timeout = 10
    frequency = 0.5
    main_page_locators = MainPageLocators()
    data = Data()

    def __init__(self, browser):
        self.browser = browser

    @allure.step("Open the page")
    def open(self, url=url):
        """this method is used to open a page"""
        self.browser.get(url)

    def wait_until_all_elements_are_visible_explicit(self, locator):
        """this method is used to wait until all elements are visible so that driver is able to interact with them"""
        return WebDriverWait(self.browser, self.timeout).until(EC.visibility_of_all_elements_located(locator))

    def wait_until_element_is_visible_explicit(self, locator):
        """this method is used to explicitly wait until an element is visible
         so that driver is able to interact with it"""
        return WebDriverWait(self.browser, self.timeout, self.frequency) \
            .until(EC.visibility_of_element_located(locator))

    def wait_until_element_is_clickable_explicit(self, locator):
        """this method is used to explicitly wait until an element is clickable
        so that driver is able to interact with it"""
        return WebDriverWait(self.browser, self.timeout, self.frequency) \
            .until(EC.element_to_be_clickable(locator))

    def get_text_explicit(self, locator):
        """this method is used to get text from an element"""
        return self.wait_until_element_is_visible_explicit(locator).text

    @allure.step("get text from a header")
    def get_header_text(self):
        """this method is used to get text from a header on the main page"""
        return self.get_text_explicit(self.main_page_locators.HEADER)

    @allure.step("push start test button")
    def click_start_test_button_explicit(self):
        """this method is used to explicitly wait until the start test button appears on the page
        and click on it"""
        self.wait_until_element_is_clickable_explicit(self.main_page_locators.START_TEST_BUTTON).click()

    @allure.step("fill out fields on the registration form")
    def fill_out_registration_fields_explicit(self):
        """this method is used to explicitly wait until registration fields appear on the page
        and then fill them out"""
        self.wait_until_element_is_visible_explicit(self.main_page_locators.LOGIN_FIELD).send_keys(self.data.LOGIN)
        self.wait_until_element_is_visible_explicit(self.main_page_locators.PASSWORD_FIELD) \
            .send_keys(self.data.PASSWORD)
        checkbox = self.wait_until_element_is_clickable_explicit(self.main_page_locators.CHECKBOX)
        with allure.step("check if the checkbox isn't selected"):
            if not self.is_checkbox_selected(self.main_page_locators.CHECKBOX):
                checkbox.click()

    def is_checkbox_selected(self, locator):
        """this method is used to check if a checkbox is selected"""
        checkbox = self.wait_until_element_is_clickable_explicit(locator)
        return checkbox.is_selected()

    @allure.step("push register button")
    def click_register_button_explicit(self):
        """this method is used to explicitly wait until the register button appears on the page
        and click on it"""
        self.wait_until_element_is_clickable_explicit(self.main_page_locators.REGISTER_BUTTON).click()

    @allure.step("make sure that the loader appears")
    def check_loader_appearance(self):
        """this method is used to check appearance of a loader after clicking on the register button"""
        return True if len(self.wait_until_all_elements_are_visible_explicit(self.main_page_locators.LOADER)) else False

    def check_success_message_appearance(self):
        """this method is used to check appearance of the success message after completing a registration"""
        return True if len(self.wait_until_all_elements_are_visible_explicit(self.main_page_locators.SUCCESS_MESSAGE)) \
            else False

    @allure.step("get text of the success message")
    def get_success_message(self):
        """this method is used to get the success message after completing a registration"""
        with allure.step("check the success message appears"):
            if self.check_success_message_appearance() is True:
                return self.get_text_explicit(self.main_page_locators.SUCCESS_MESSAGE)
            else:
                return "There's no success message"

    def get_text_implicit(self, locator):
        """this method is used to get text from an element"""
        return self.browser.find_element(*locator).text

    @allure.step("get text from a header")
    def get_header_text_implicit(self):
        """this method is used to get text from a header on the main page"""
        return self.get_text_explicit(self.main_page_locators.HEADER)

    @allure.step("push start test button")
    def click_start_test_button_implicit(self):
        """this method is used to implicitly wait until the start test button appears on the page
        and click on it"""
        self.browser.find_element(*self.main_page_locators.START_TEST_BUTTON).click()

    @allure.step("fill out fields on the registration form")
    def fill_out_registration_fields_implicit(self):
        """this method is used to implicitly wait until registration fields appear on the page
        and then fill them out"""
        self.browser.find_element(*self.main_page_locators.LOGIN_FIELD).send_keys(self.data.LOGIN)
        self.browser.find_element(*self.main_page_locators.PASSWORD_FIELD) \
            .send_keys(self.data.PASSWORD)
        checkbox = self.browser.find_element(*self.main_page_locators.CHECKBOX)
        with allure.step("check if the checkbox isn't selected"):
            if not self.is_checkbox_selected_implicit(self.main_page_locators.CHECKBOX):
                checkbox.click()

    def is_checkbox_selected_implicit(self, locator):
        """this method is used to check if a checkbox is selected"""
        checkbox = self.browser.find_element(*locator)
        return checkbox.is_selected()

    @allure.step("push register button")
    def click_register_button_implicit(self):
        """this method is used to implicitly wait until the register button appears on the page
        and click on it"""
        self.browser.find_element(*self.main_page_locators.REGISTER_BUTTON).click()

    @allure.step("make sure that the loader appears")
    def check_loader_appearance_implicit(self):
        """this method is used to check appearance of a loader after clicking on the register button"""
        return True if len(self.browser.find_elements(*self.main_page_locators.LOADER)) else False

    def check_success_message_appearance_implicit(self):
        """this method is used to check appearance of the success message after completing a registration"""
        return True if len(self.browser.find_elements(self.main_page_locators.SUCCESS_MESSAGE)) \
            else False

    @allure.step("get text of the success message")
    def get_success_message_implicit(self):
        """this method is used to get the success message after completing a registration"""
        with allure.step("check the success message appears"):
            if self.check_success_message_appearance() is True:
                return self.get_text_implicit(self.main_page_locators.SUCCESS_MESSAGE)
            else:
                return "There's no success message"
