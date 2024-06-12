from pydantic import BaseModel, field_validator


class Category(BaseModel):
    id: int
    name: str


class Tag(BaseModel):
    id: int
    name: str


class CreatePetSchema(BaseModel):
    id: int
    name: str
    category: Category
    photoUrls: list[str] = []
    tags: list[Tag] = []
    status: str

    @field_validator("status")
    def validate_status(cls, v: str) -> str:
        if v not in ["available", "pending", "sold"]:
            raise ValueError(f"Invalid status: {v}, available, pending or sold expected")
        return v
