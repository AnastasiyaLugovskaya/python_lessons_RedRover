import json

import allure
from requests import Response


class BaseTestData:
    @staticmethod
    def convert_data_to_json(data):
        json_data = json.dumps(data)
        return json_data

    @staticmethod
    def attach_request(request):
        request = json.dumps(json.loads(request.json()), indent=4)
        allure.attach(body=request, name="Request", attachment_type=allure.attachment_type.JSON)

    @staticmethod
    def attach_response(response: Response):
        response = json.dumps(response.json(), indent=4)
        allure.attach(body=response, name="Response", attachment_type=allure.attachment_type.JSON)
