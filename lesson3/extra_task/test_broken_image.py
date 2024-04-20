import allure
import pytest

from lesson3.extra_task.broken_page import BrokenPage
from lesson3.extra_task.functions import get_key_by_value


@allure.epic('Testing images on the page')
class TestBrokenImage:
    @allure.title("Test there are no broken images on the page")
    @pytest.mark.xfail
    def test_no_broken_images(self, browser):
        page = BrokenPage(browser)
        good_img_dict = page.open().check_image()
        assert False not in good_img_dict.values(), f"There are broken images on the page: numbers of broken images " \
                                                    f"{get_key_by_value(good_img_dict)}"
