import allure
import pytest

from petstore_api.data import get_pet_endpoints
from petstore_api.data.data import Data
from petstore_api.src.assertions import Assertion
from petstore_api.src.http_methods import MyRequests
from http import HTTPStatus
from petstore_api.src.prepared_data.prepared_pet_data import PreparedPetData
from petstore_api.src.schemas import CreatePetSchema
from petstore_api.src.validator import Validator
from petstore_api.generator.pet_generator import PetGenerator


@allure.epic("Testing pet creation")
class TestCreatePet:
    request = MyRequests()
    url = get_pet_endpoints()
    assertion = Assertion()
    validator = Validator()
    pet_data = PreparedPetData()
    pet_generator = PetGenerator()

    @allure.title("Create pet with valid status")
    @pytest.mark.parametrize("status", Data.statuses)
    def test_create_pet_with_valid_status(self, get_test_name, status):
        info = next(self.pet_generator.generate_pet(url_count=2, status=status))
        data = self.pet_data.prepare_pet_json(info=info)
        response = self.request.post(url=self.url.create_pet, data=data)
        print(response.text)
        self.assertion.assert_status_code(response, HTTPStatus.OK, get_test_name)
        self.validator.validate_response(response=response, model=CreatePetSchema.create_pet)

    @allure.title("Create pet with invalid status")
    def test_create_pet_with_invalid_status(self, get_test_name):
        info = next(self.pet_generator.generate_pet(url_count=2, status="Wrong status"))
        data = self.pet_data.prepare_pet_json(info=info)
        response = self.request.post(url=self.url.create_pet, data=data)
        print(response.text)
        self.assertion.assert_status_code(response, HTTPStatus.BAD_REQUEST, get_test_name)
        self.validator.validate_response(response=response, model=CreatePetSchema.create_pet)
#         остановилась на лекции 16.1 (05/19) Тестирование API (Denis Tadzhibaev) 58:40
