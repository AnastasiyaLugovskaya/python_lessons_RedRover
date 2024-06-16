from dataclasses import dataclass

from petstore_api.src.schemas.pet_request_schema import Category


@dataclass
class PetDataClass:
    uid: int
    category: Category
    name: str
    photo_urls: list[str]
    tags: list
    status: str
