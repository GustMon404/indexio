from pydantic import BaseModel


class Message(BaseModel):
    message: str


class Field(BaseModel):
    label: str
    field: str
    description: str


class Document(BaseModel):
    fields: list[Field]
    text_plain: str
