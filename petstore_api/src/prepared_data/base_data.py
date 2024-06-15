import json


class BaseTestData:
    @staticmethod
    def convert_data_to_json(data):
        json_data = json.dumps(data)
        return json_data
