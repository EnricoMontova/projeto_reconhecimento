import cv2
import os
import json
from ultralytics import YOLO
from groq import Groq
from dotenv import load_dotenv

# 1. Carrega as credenciais
load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# 2. Inicializa o modelo visual e as pastas
modelo = YOLO("yolov8n.pt")
pasta_entrada = "imagens_entrada"
pasta_saida = "resultados"

dados_totais_para_llm = {}

print(f"Iniciando análise visual na pasta '{pasta_entrada}'...\n")

# 3. Processamento e Extração de Dados
for nome_arquivo in os.listdir(pasta_entrada):
    if nome_arquivo.lower().endswith(('.jpg', '.jpeg', '.png')):
        caminho_imagem = os.path.join(pasta_entrada, nome_arquivo)
        imagem = cv2.imread(caminho_imagem)
        
        if imagem is not None:
            print(f"Analisando: {nome_arquivo}...")
            resultados = modelo(imagem, conf=0.5)
            
            objetos_detectados = []
            
            # Extrai o nome e a confiança de cada objeto encontrado
            for box in resultados[0].boxes:
                classe_id = int(box.cls[0])
                nome_classe = modelo.names[classe_id]
                confianca = float(box.conf[0])
                
                objetos_detectados.append({
                    "objeto": nome_classe,
                    "confianca": round(confianca, 2)
                })
            
            dados_totais_para_llm[nome_arquivo] = objetos_detectados
            
            # Salva a imagem com os retângulos desenhados
            imagem_anotada = resultados[0].plot()
            cv2.imwrite(os.path.join(pasta_saida, nome_arquivo), imagem_anotada)

print("\nImagens processadas. Iniciando análise gerativa via Groq...\n")

# 4. Serialização do Resultado Visual para JSON
payload_json = json.dumps(dados_totais_para_llm, ensure_ascii=False, indent=2)

# 5. Construção do Prompt guiando a análise
prompt_usuario = f"""
Aqui estão os resultados de um sistema de Visão Computacional (YOLOv8) monitorando um ambiente. 
Os dados estão organizados por arquivo, contendo os objetos detectados e o nível de confiança.

Analise estes dados estruturados e forneça:
1. Um panorama geral do que está presente nas imagens.
2. Identificação de padrões ou situações de alerta (anomalias).
3. Recomendações de ação com base nos objetos encontrados.

Dados extraídos:
{payload_json}
"""

# 6. Chamada à LLM
resposta = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "Você é um sistema inteligente especialista em análise de dados de sensores e automação industrial. Responda em tópicos claros e objetivos."},
        {"role": "user", "content": prompt_usuario}
    ],
    temperature=0.2,
)

# 7. Apresentação do Resultado
analise_final = resposta.choices[0].message.content

print("="*50)
print("RELATÓRIO DE INTELIGÊNCIA - GROQ")
print("="*50)
print(analise_final)
print("="*50)