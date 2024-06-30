from openai import OpenAI


def extract_data(prompt_system: str, prompt_user: str) -> str:
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

    return response.choices[0].message.content


def get_prompt_system(list_fields: list[dict]) -> str:
    prompt = f""""
            Extraia o {', '.join([field['label'] for field in list_fields])} do texto.
            Retorne apenas no formato json:
            {', '.join(['{"%s": "%s"}' % (field['field'], field['description']) for field in list_fields])}
            Obs: Não escreva nada antes e tbm não escreva nada depois."""
    print(prompt)
    return prompt


def set_index_document(list_fields, text):
    prompt_user = get_prompt_system(list_fields)
    return extract_data(prompt_user, text)
