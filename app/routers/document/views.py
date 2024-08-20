from fastapi import APIRouter, Depends

from .schemas import *
from celery import shared_task
from .services import process_and_store_extracted_info

router = APIRouter(prefix='/document')


@shared_task
def teste():
    print("oi")


@router.post('/extract', response_model=Message)
async def extract(document: Document):
    list_fields = document.model_dump()['fields']
    text = document.model_dump()['text_plain']
    type_form = document.model_dump()['type_form']
    document_id = await process_and_store_extracted_info(list_fields, text, type_form)
    return {'message': document_id}
    # teste.delay()
    # return {'message': 'teste'}



