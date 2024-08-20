# IndexIO
Destina-se a extrair dados relevantes de um texto conforme o critério de indexação,
utilizando uma LLM.

## Requeriments

---

Antes de Prosseguir, garanta que esses recursos estejam instalados.

* [Python 3.8+](https://www.python.org/downloads/)
* [Docker](https://www.docker.com/)
* [Poetry](https://python-poetry.org/docs/#installation)
* [Ollama](https://ollama.com/download)
* [MongoDB Compass](https://www.mongodb.com/try/download/compass) (Opcional)
* WSL (Windows)

### Instalação LLM

---

Esse Projeto, está utilizando o modelo llama3 de 8B. Faça a instalação através da linha de comando:

````bash
ollama run llama3
````

### Instalação RabbitMQ

---

Instalação necessária para executar o celery

````bash
docker run -d -p 5672:5672 rabbitmq
````

### Instalação MongoDb

---

````bash
docker run --name mongodb -p 27017:27017 -d mongodb/mongodb-community-server:latest

````

## QuickStart

---

### Inicie uma máquina Virtual com Poetry

Execute o seguinte comando para criar uma virtualenv


````bash
poetry shell

````

Em seguida, instale as depêndências


````bash
poetry install

````

### Adicione as variáveis de ambiente

Crie o arquivo arquivo `.env` e adicione as seguintes variáveis
>MONGODB_URL= <br>
>DB_NAME=

### Inicie o celery
````bash

````

### Inicie o Projeto
````bash
fastapi dev app/main.py
````