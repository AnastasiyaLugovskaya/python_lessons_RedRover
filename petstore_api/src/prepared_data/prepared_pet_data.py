from petstore_api.data.pet_data_class import PetDataClass
from petstore_api.src.prepared_data.base_data import BaseTestData


class PreparedPetData(BaseTestData):

    def prepare_pet_json(self, info: PetDataClass):
        # json_data = get_json_data(json_data="pet_data.json")
        # return json_data
        data = {
            "id": info.uid,
            "name": info.name,
            "category": info.category,
            "photoUrls": info.photo_urls,
            "tags": info.tags,
            "status": info.status
        }
        return self.convert_data_to_json(data)
