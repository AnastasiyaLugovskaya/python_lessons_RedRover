import allure
import requests
from requests import Response
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from lesson3.extra_task.pages.base_page import BasePage
from lesson3.extra_task.locators.broken_page_locators import BrokenPageLocators
from lesson3.extra_task.urls import Url
from selenium.common import NoSuchElementException
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class BrokenPage(BasePage):
    timeout = 10
    locators = BrokenPageLocators()

    def __init__(self, browser):
        super().__init__(browser)
        self.url = Url.BROKEN_IMAGE_PAGE_URL

    @allure.step("Find all images on the page")
    def get_image_list(self) -> list[WebElement]:
        """this method is used to find all images on the page and return them as a lis of web elements"""
        try:
            image_list = WebDriverWait(self.browser, self.timeout) \
                .until(EC.visibility_of_all_elements_located(self.locators.IMAGES))
        except(NoSuchElementException, TimeoutException):
            image_list = []
        return image_list

    @allure.step("Get 'src' attributes from images")
    def get_src_attribute(self, image_list: list[WebElement]) -> list[str]:
        """this method is used to get value of 'src' attribute from <img> elements in the given list"""
        src_list = []
        if len(image_list) > 0:
            for i in image_list:
                src_list.append(i.get_attribute("src"))
        return src_list

    @allure.step("Get server response")
    def get_server_response(self, src_list: list) -> list[Response]:
        """this method is used for sending a request with url from src list to the server and getting a response"""
        response_list = []
        if len(src_list) > 0:
            for i in src_list:
                response = requests.get(i)
                response_list.append(response)
        return response_list

    @allure.step("Get status code for each image")
    def get_status_code(self, response_list: list[Response]) -> list[int]:
        """this method is used to get a status code from each response in the list"""
        status_code_list = []
        if len(response_list) > 0:
            for i in response_list:
                code = i.status_code
                status_code_list.append(code)
        return status_code_list

    @allure.step("Check each image isn't broken")
    def check_image(self) -> dict:
        """this method is used to check each image in te list"""
        image_list = self.get_image_list()
        srs_list = self.get_src_attribute(image_list)
        responses = self.get_server_response(srs_list)
        status_code_list = self.get_status_code(responses)
        images = dict()
        counter = 1
        if len(status_code_list) > 0:
            for i in status_code_list:
                if i != 200:
                    images[counter] = False
                else:
                    images[counter] = True
                counter += 1
        return images
