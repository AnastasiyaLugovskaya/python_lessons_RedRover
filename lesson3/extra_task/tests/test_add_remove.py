import random

import allure

from lesson3.extra_task.pages.add_page import AddPage


@allure.epic("Testing adding and removing an element")
class TestAddRemove:
    number = random.randint(1, 10)

    @allure.title("Test adding an element")
    def test_add_element(self, browser):
        page = AddPage(browser)
        actual_number_of_elements = page.open()\
            .click_on_add_button(self.number)\
            .get_number_of_added_elements()
        assert actual_number_of_elements == self.number, "There weren't all elements added." \
            f" Expected number of elements = {self.number}, actual number = {actual_number_of_elements}"

    @allure.title("Test removing an element")
    def test_remove_element(self, browser):
        page = AddPage(browser)
        is_page_clear = page.open()\
            .click_on_add_button(self.number)\
            .click_on_delete_button(self.number)\
            .check_the_page_has_no_elements()
        assert is_page_clear is True, "There are still elements on the page."
