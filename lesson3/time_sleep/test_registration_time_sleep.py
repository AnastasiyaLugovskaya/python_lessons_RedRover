import time

import allure

from lesson3.main_page import MainPage


@allure.epic("Test using time.sleep()")
class TestRegistrationTimeSleep:
    @allure.title("registration with waits based on time.sleep()")
    def test_registration_time_sleep(self, browser):
        page = MainPage(browser)
        page.open()
        time.sleep(5)
        header_text = page.get_header_text_implicit()
        expected_text = 'Практика с ожиданиями в Selenium'
        assert header_text == expected_text, "The actual header doesn't match the expected one." \
                                             f"Expected header is '{expected_text}', actual is '{header_text}"
        page.click_start_test_button_implicit()
        time.sleep(5)
        page.fill_out_registration_fields_implicit()
        page.click_register_button_implicit()
        time.sleep(5)
        loader_appeared = page.check_loader_appearance_implicit()
        assert loader_appeared is True, "The loader didn't appear"
        time.sleep(5)
        success_message = page.get_success_message_implicit()
        expected_message = 'Вы успешно зарегистрированы!'
        assert success_message == expected_message, "The actual message doesn't match the expected one." \
            f"Expected message is '{expected_message}', actual message is '{success_message}'"
