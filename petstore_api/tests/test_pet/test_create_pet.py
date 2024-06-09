import allure

from petstore_api.data import get_pet_endpoints
from petstore_api.src.assertions import Assertion
from petstore_api.src.http_methods import MyRequests
from http import HTTPStatus


@allure.epic("Testing pet creation")
class TestCreatePet:
    request = MyRequests()
    url = get_pet_endpoints()
    assertion = Assertion()

    def test_create_pet(self, get_test_name):
        data = """{
            "id": 55,
            "category": {
                "id": 56,
                "name": "pokemon"
            },
            "name": "Bulbasaur",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 5,
                    "name": "pokemon"
                }
            ],
            "status": "available"
        }"""
        response = self.request.post(url=self.url.create_pet, data=data)
        print(response.text)
        self.assertion.assert_status_code(response, HTTPStatus.CREATED, get_test_name)
