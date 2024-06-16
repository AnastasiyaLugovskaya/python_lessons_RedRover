from petstore_api.data.pet_data_class import PetDataClass
from petstore_api.src.prepared_data.base_data import BaseTestData
from petstore_api.src.schemas.pet_request_schema import PetRequestSchema


class PreparedPetData(BaseTestData):

    def prepare_pet_json(self, info: PetDataClass, key=None):
        # option 1
        # json_data = get_json_data(json_data="pet_data.json")
        # return json_data
        # option 2
        # data = {
        #     "id": info.uid,
        #     "name": info.name,
        #     "category": info.category,
        #     "photoUrls": info.photo_urls,
        #     "tags": info.tags,
        #     "status": info.status
        # }
        # if key is not None:
        #     data.pop(key, None)
        # return self.convert_data_to_json(data)
        # option 3
        data = PetRequestSchema(
            id=info.uid,
            name=info.name,
            category=info.category,
            photoUrls=info.photo_urls,
            tags=info.tags,
            status=info.status
        )
        self.attach_request(data)
        return data.json()
