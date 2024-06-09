from requests import Response
from petstore_api.src.logger import get_logger


class Assertion:
    @staticmethod
    def assert_status_code(response: Response, expected_status_code: int, test_name: str):
        actual_status_code = response.status_code
        assert expected_status_code == actual_status_code, (
            get_logger(test_name).error(
                f"Expected status code: {expected_status_code}, actual status code: {actual_status_code}"
            )
        )
