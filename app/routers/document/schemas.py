from pydantic import BaseModel


class Message(BaseModel):
    message: str


class Field(BaseModel):
    label: str
    field: str
    description: str


class Document(BaseModel):
    type_form: str
    fields: list[Field]
    text_plain: str
