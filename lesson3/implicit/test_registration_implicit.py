from lesson3.main_page import MainPage
import allure


@allure.epic("Test using implicit waits")
class TestRegistrationImplicit:
    @allure.title("registration with implicit waits")
    def test_registration_implicit(self, browser):
        page = MainPage(browser)
        page.open()
        header_text = page.get_header_text_implicit()
        expected_text = 'Практика с ожиданиями в Selenium'
        assert header_text == expected_text, "The actual header doesn't match the expected one." \
                                             f"Expected header is '{expected_text}', actual is '{header_text}"
        page.click_start_test_button_implicit()
        page.fill_out_registration_fields_implicit()
        page.click_register_button_implicit()
        loader_appeared = page.check_loader_appearance_implicit()
        assert loader_appeared is True, "The loader didn't appear"
        success_message = page.get_success_message_implicit()
        expected_message = 'Вы успешно зарегистрированы!'
        assert success_message == expected_message, "The actual message doesn't match the expected one." \
            f"Expected message is '{expected_message}', actual message is '{success_message}'"
