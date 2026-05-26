# 👁️ Reconhecimento de Objetos em Lote com YOLOv8

Este repositório contém a entrega final do projeto de Reconhecimento de Objetos, implementado em Python. O objetivo principal é demonstrar o domínio sobre algoritmos de visão computacional através de um pipeline automatizado de inferência em lote.

## 🚀 Sobre o Projeto

Em vez de utilizar uma abordagem comum de análise via webcam em tempo real, este projeto foca em **processamento em lote (Batch Processing)**. O script varre automaticamente um diretório de imagens de entrada, aplica o modelo de Inteligência Artificial para detectar múltiplas classes (pessoas, veículos, objetos do dia a dia, etc.) e exporta os resultados anotados para um diretório de saída.

### Por que o YOLOv8 Nano?
Para esta demanda, a escolha técnica foi o modelo **YOLOv8 na versão Nano (`yolov8n.pt`)**. A justificativa baseia-se em três pilares:
1. **Arquitetura State-of-the-Art:** O YOLOv8 utiliza uma arquitetura *anchor-free*, garantindo alta precisão na detecção de bordas e centros dos objetos.
2. **Desempenho em CPU:** A versão Nano é leve o suficiente para rodar inferências rápidas em processadores comuns, sem a necessidade de hardware dedicado (GPU).
3. **Escopo e Estabilidade:** Entre as opções de YOLO (v5, v8, v11), a versão 8 apresenta a maior maturidade, documentação consolidada e integração fluida com o Python.

## 📁 Estrutura do Repositório

* `recom.py`: Script principal em Python contendo o motor de automação e inferência.
* `imagens_entrada/`: Diretório onde as imagens brutas devem ser alocadas antes da execução.
* `resultados/`: Diretório gerado automaticamente (ou utilizado) para salvar as imagens processadas com as bounding boxes (caixas delimitadoras).

## 🛠️ Tecnologias Utilizadas

* **Python 3.14.2
* **Ultralytics (YOLOv8):** Responsável pelo modelo de Deep Learning e cálculos de predição.
* **OpenCV (`cv2`):** Atua na camada de manipulação de imagem, extração de dados (pixels) e gravação em disco.
* **OS:** Biblioteca nativa do Python para navegação e automação de diretórios.

## ⚙️ Como Executar

**1. Instale as dependências:**
Certifique-se de ter o Python instalado. No terminal, execute:
```bash
pip install ultralytics opencv-python
