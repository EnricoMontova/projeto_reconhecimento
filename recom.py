import cv2
import os
from ultralytics import YOLO

# 1. Carrega o modelo YOLOv8 leve
modelo = YOLO("yolov8n.pt")

# 2. Define as pastas de origem e destino
pasta_entrada = "imagens_entrada"
pasta_saida = "resultados"

print(f"Iniciando análise em lote na pasta '{pasta_entrada}'...\n")

# 3. Lê todos os arquivos dentro da pasta de entrada
for nome_arquivo in os.listdir(pasta_entrada):
    # Verifica se o arquivo é uma imagem válida
    if nome_arquivo.lower().endswith(('.jpg', '.jpeg', '.png')):
        caminho_imagem = os.path.join(pasta_entrada, nome_arquivo)
        
        # Lê a imagem
        imagem = cv2.imread(caminho_imagem)
        
        if imagem is not None:
            print(f"Analisando: {nome_arquivo}...")
            
            # Executa o reconhecimento
            resultados = modelo(imagem, conf=0.5)
            
            # Desenha as anotações
            imagem_anotada = resultados[0].plot()
            
            # Salva a imagem final na pasta de resultados
            caminho_salvar = os.path.join(pasta_saida, nome_arquivo)
            cv2.imwrite(caminho_salvar, imagem_anotada)

print("\nSucesso! Todas as imagens foram processadas e salvas na pasta 'resultados'.")