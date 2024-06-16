import json

import allure
from requests import Response


class BaseModule:
    @staticmethod
    def attach_request(request):
        request = json.dumps(json.loads(request.json()), indent=4)
        allure.attach(body=request, name="Request", attachment_type=allure.attachment_type.JSON)

    @staticmethod
    def attach_response(response: Response):
        response = json.dumps(response.json(), indent=4)
        allure.attach(body=response, name="Response", attachment_type=allure.attachment_type.JSON)
