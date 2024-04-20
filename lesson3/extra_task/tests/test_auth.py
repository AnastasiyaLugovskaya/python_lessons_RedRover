import allure

from lesson3.extra_task.pages.auth_page import AuthPage


@allure.epic("Testing Authentication alerts")
class TestAuth:
    expected_text = 'Congratulations! You must have the proper credentials.'
    valid_auth_data = 'admin'
    invalid_auth_data = ('wrong', 'data')

    @allure.title("Test successful authorization by passing credentials in url")
    def test_authorize_by_passing_credentials_in_url(self, browser):
        page = AuthPage(browser)
        congrat_text = page \
            .pass_auth_data_in_url() \
            .get_congratulation_text()
        assert congrat_text == self.expected_text, "There's no congratulation message." \
             f" Expected text is '{self.expected_text}', actual text is '{congrat_text}'"

    @allure.title("Test authorization with valid credentials")
    def test_authorize_by_passing_valid_data(self, browser):
        page = AuthPage(browser)
        congrat_text = page.open() \
            .base_auth(self.valid_auth_data, self.valid_auth_data) \
            .get_congratulation_text()
        assert congrat_text == self.expected_text, "There's no congratulation message." \
             f" Expected text is '{self.expected_text}', actual text is '{congrat_text}'"

    @allure.title("Test authorization with wrong credentials")
    def test_authorize_by_passing_invalid_data(self, browser):
        page = AuthPage(browser)
        response = page\
            .open()\
            .get_response(self.invalid_auth_data[0], self.invalid_auth_data[1])
        status_code = page.get_status_code(response)
        assert status_code == 401, f"Unexpected status code! Expected code = 401, actual = {status_code}"
