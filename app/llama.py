from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama',  # required, but unused
)

prompt_system = """Extraia o Nome, Data do texto
                    Retorne apenas no formato json:
                    {
                        "nome": "nome do paciente",
                        "data_consulta": "pattern: 2000-05-06T00:00:00"
                    }
                    
                    Obs: Não escreva nada antes e tbm não escreva nada depois.
                    """

prompt_user = "Nome do Paciente: Maria de Souza Silva Data de Nascimento: 22/05/1980 CPF: 987.654.321-00 RG: 21.543.678-0 Endereço: Rua das Flores, 321, Apto 202, Centro, Rio de Janeiro, RJ, 20000-000 Telefone: (21) 2345-6789 Celular: (21) 98765-4321 E-mail: maria.silva@email.com Data da Consulta: 25/06/2024 Médico Responsável: Dr. João Carlos Pereira Especialidade: Cardiologia Motivo da Consulta: Dor no peito e falta de ar Histórico Médico: Hipertensão, Diabetes Tipo 2 Medicamentos em Uso: Losartana 50mg, Metformina 850mg Exames Solicitados: Eletrocardiograma, Exame de Sangue, Teste de Esforço Diagnóstico: Angina Estável Tratamento Prescrito: Ajuste na medicação para hipertensão, Iniciar uso de AAS 100mg, Recomendação de atividade física moderada Observações: Paciente deve retornar em 30 dias para reavaliação"

response = client.chat.completions.create(
    model="llama3",
    messages=[
        {"role": "system", "content": prompt_system},
        {"role": "user", "content": prompt_user},
    ],
    response_format={"type": "json_object"},
)
print(response.choices[0].message.content,type(response.choices[0].message.content))
