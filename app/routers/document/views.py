from fastapi import APIRouter

from .schemas import *
from .service import set_index_document

router = APIRouter(prefix='/document')


@router.post('/extract', response_model=Message)
def extract(document: Document):
    list_fields = document.model_dump()['fields']
    text = document.model_dump()['text_plain']
    teste = set_index_document(list_fields, text)
    return {'message': teste}
