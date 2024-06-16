from pydantic import BaseModel, field_validator


class Category(BaseModel):
    id: int
    name: str


class Tag(BaseModel):
    id: int
    name: str


class PetRequestSchema(BaseModel):
    id: int
    name: str
    category: Category
    photoUrls: list[str] = []
    tags: list[Tag] = []
    status: str
