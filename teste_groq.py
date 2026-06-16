import os
from dotenv import load_dotenv
from groq import Groq

# 1. Carrega as configurações ocultas do arquivo .env
load_dotenv()

# 2. Conecta ao Groq usando a sua chave
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

print("Conectando ao Groq... Aguarde um instante.\n")

# 3. Faz uma requisição simples de teste
resposta = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": "Diga 'Olá, mundo! Sua chave da API está funcionando perfeitamente!' e me dê uma explicação de uma linha sobre o maior benefício do Cloud Computing."}
    ],
    temperature=0.5
)

# 4. Imprime o resultado na tela
print("RESPOSTA DA IA:")
print("-" * 40)
print(resposta.choices[0].message.content)
print("-" * 40)