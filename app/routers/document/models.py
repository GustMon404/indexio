from typing import Optional, Annotated, ClassVar
from bson import ObjectId

from pydantic import BaseModel, Field, BeforeValidator, ConfigDict

from .constants import STATUS

PyObjectId = Annotated[str, BeforeValidator(str)]


class FieldModel(BaseModel):
    label: str
    field: str
    description: str


class DocumentLogCollection(BaseModel):
    collection_name: ClassVar[str] = 'document_log'

    id: Optional[PyObjectId] = Field(alias='_id', default=None)
    input_fields: list[FieldModel]
    text: str
    status: STATUS = STATUS.PENDING
    type_form: str
    result: Optional[dict] = None
    choice: Optional[dict] = None

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )


class ErrorLogCollection(BaseModel):
    collection_name: ClassVar[str] = 'error_log'

    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    id_document_log: int
    message: str

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )
