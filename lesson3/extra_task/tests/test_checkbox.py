import allure

from lesson3.extra_task.pages.checkbox_page import CheckboxPage


@allure.epic("Testing checkboxes")
class TestCheckbox:
    @allure.title("Test the first checkbox is not checked after opening a page")
    def test_first_checkbox_not_checked(self, browser):
        page = CheckboxPage(browser)
        is_checked = page.open().check_checkbox_condition(num=1)
        assert is_checked is False, "The first checkbox is already checked, but shouldn't be"

    @allure.title("Test the second checkbox is already checked after opening a page")
    def test_second_checkbox_is_checked(self, browser):
        page = CheckboxPage(browser)
        is_checked = page.open().check_checkbox_condition(num=2)
        assert is_checked is True, "The second checkbox isn't checked, but should be"

    @allure.title("Test successful selection of a checkbox")
    def test_select_checkbox(self, browser):
        page = CheckboxPage(browser)
        is_checked = page.open().check_checkbox_condition(num=1)
        if not is_checked:
            page.check_the_box(num=1)
            is_checked = page.check_checkbox_condition(num=1)
            assert is_checked is True, "Checkbox isn't selected!"
        else:
            print("Checkbox has been already checked!")

    @allure.title("Test successful deselection of a checkbox")
    def test_deselect_checkbox(self, browser):
        page = CheckboxPage(browser)
        is_checked = page.open().check_checkbox_condition(num=2)
        if is_checked:
            page.check_the_box(num=2)
            is_checked = page.check_checkbox_condition(num=2)
            assert is_checked is False, "Checkbox is still selected!"
        else:
            print("Checkbox has been already deselected!")
