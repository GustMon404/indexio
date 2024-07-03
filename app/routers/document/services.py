from openai import OpenAI
from app.routers.document.models import DocumentLogCollection, ErrorLogCollection
from app.config.mongodb import database as db_mongo
from bson import ObjectId
from app.routers.document.constants import STATUS, ERROR_TYPE

from app import utils


async def extract_information_from_text(prompt_system: str, prompt_user: str, document_id: str):
    async def store_result(result):
        if json_dict := utils.get_json_if_valid(result):
            await update_document(ObjectId(document_id), status=STATUS.FINISHED, result=json_dict)
        else:
            await add_error_log(ObjectId(document_id), ERROR_TYPE.JSON_INVALID, msg=result)
            await update_document(ObjectId(document_id), status=STATUS.ERROR)

    await update_document(ObjectId(document_id), status=STATUS.PROCESSING)

    client = OpenAI(
        base_url='http://localhost:11434/v1',
        api_key='ollama',  # required, but unused
    )

    response = client.chat.completions.create(
        model="llama3",
        messages=[
            {"role": "system", "content": prompt_system},
            {"role": "user", "content": prompt_user},
        ],
        response_format={"type": "json_object"},
    )

    await store_result(response.choices[0].message.content)


def get_prompt_system(list_fields: list[dict]) -> str:
    prompt = f""""
            Extraia o {', '.join([field['label'] for field in list_fields])} do texto.
            Retorne apenas no formato json:
            {', '.join(['{"%s": "%s"}' % (field['field'], field['description']) for field in list_fields])}
            Obs: Não escreva nada antes e tbm não escreva nada depois."""
    return prompt


async def process_and_store_extracted_info(list_fields: list[dict], text: str, type_form: str) -> str:
    document_log_id = await add_document(list_fields, text, type_form)
    prompt_user = get_prompt_system(list_fields)
    # document = await get_document(document_log_id)
    await extract_information_from_text(prompt_user, text, document_log_id)
    return str(document_log_id)
    # return extract_data(prompt_user, text, document_log_id)


async def add_document(list_fields: list[dict], text: str, type_form: str):
    doc = DocumentLogCollection(type_form=type_form, input_fields=list_fields, text=text)
    document_collection = db_mongo.db.get_collection(DocumentLogCollection.collection_name)
    new_doc = await document_collection.insert_one(doc.model_dump(by_alias=True, exclude={'id'}))
    return new_doc.inserted_id


async def get_document(id_document: ObjectId):
    document_collection = db_mongo.db.get_collection(DocumentLogCollection.collection_name)
    document = await document_collection.find_one({'_id': id_document})
    return document


async def update_document(id_document: ObjectId, status: STATUS = None, result: dict = None, choice: dict = None):
    dict_field_upload = utils.remove_value_none_from_dict({'status': status, 'result': result, 'choice': choice})
    document_collection = db_mongo.db.get_collection(DocumentLogCollection.collection_name)
    update_result = await document_collection.find_one_and_update(
        {"_id": id_document},
        {"$set": dict_field_upload}
    )

    if update_result is not None:
        return update_result


async def add_error_log(id_document: ObjectId, error_type: ERROR_TYPE, msg: str):
    error = ErrorLogCollection(id_document=id_document, error_type=error_type, message=msg)
    error_collection = db_mongo.db.get_collection(ErrorLogCollection.collection_name)
    await error_collection.insert_one(error.model_dump(by_alias=True, exclude={'id'}))
