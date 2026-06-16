# 👁️ Evolução do Pipeline: Da Visão Computacional Local à Análise Generativa em Nuvem

Este repositório documenta a jornada de desenvolvimento de um ecossistema de automação visual inteligente. O projeto nasceu como um motor de processamento local para reconhecimento de padrões e evoluiu para uma arquitetura **Edge-to-Cloud**, capaz não apenas de detectar objetos, mas de interpretar cenários e gerar relatórios táticos para suporte à decisão em ambientes de TI e automação industrial.

---

## 🏁 Fase 1: Detecção Visual Autônoma (O Módulo Base)

Na sua primeira iteração, o foco do sistema era a automação do reconhecimento espacial e a extração gráfica de dados. 

O script inicial (`recom.py`) foi desenhado como um motor de inferência local otimizado para **processamento em lote (Batch Processing)**. O fluxo consistia em varrer um diretório de imagens originais, aplicar um filtro condicional para arquivos válidos (`.jpg`, `.jpeg`, `.png`) e processá-los sequencialmente.

Nesta etapa, o pipeline executava três tarefas principais:
1. **Conversão:** Transformação da imagem em matrizes numéricas nativas usando OpenCV.
2. **Inferência:** Execução do modelo YOLOv8 com um limite de confiança estrito (`conf=0.5`) para mitigar falsos positivos.
3. **Anotação Gráfica:** Desenho das caixas delimitadoras (*bounding boxes*) e índices de acerto sobre a imagem, salvando o resultado visual na pasta de saída.

Apesar de altamente eficiente na detecção gráfica, os dados gerados eram puramente visuais, exigindo interpretação humana direta.

---

## 🚀 Fase 2: O Salto Cognitivo (Integração Edge-to-Cloud)

Para elevar o projeto ao patamar de **Sistemas Inteligentes**, a Fase 2 (`recom_groq.py`) introduziu uma camada de Inteligência Artificial Generativa. O pipeline deixou de ser apenas um extrator gráfico e passou a funcionar como um integrador cognitivo.

Nesta arquitetura atualizada, a telemetria visual coletada na borda (Edge) alimenta um modelo de linguagem na nuvem (Cloud) em tempo real:

1. **Extração de Telemetria Visual:** Em vez de apenas gerar uma imagem desenhada, o sistema agora intercepta as propriedades do YOLOv8, extraindo o ID numérico, a tradução textual da classe e o índice estatístico de certeza de cada objeto.
2. **Contrato de Dados e Serialização:** Para viabilizar o tráfego veloz para a nuvem, essa telemetria é encapsulada em um dicionário Python e serializada no formato **JSON** (`json.dumps()`), criando uma ponte universal e estruturada entre a visão local e o cérebro em nuvem.
3. **Engenharia de Prompt e Contexto:** A comunicação com a LLM é blindada por um *System Prompt* rigoroso, obrigando a IA a agir exclusivamente como um analista de automação industrial. O *User Prompt* injeta o JSON e exige saídas táticas (Panorama, Anomalias e Recomendações).
4. **Inferência e Controle de Entropia:** A requisição é enviada ao modelo **Llama 3.3 70B** na infraestrutura da Groq com a temperatura cravada em `0.2`. Isso garante respostas puramente factuais, lógicas e determinísticas, neutralizando o risco de alucinações.

---

## 🛠️ Stack Tecnológico Consolidado

A engenharia final do projeto equilibra o processamento na máquina local com a escalabilidade da computação em nuvem:

* **Python & python-dotenv:** Orquestração do fluxo de execução e isolamento seguro de credenciais (API Keys).
* **Ultralytics YOLOv8 (`yolov8n.pt`):** Motor de *Deep Learning* (versão Nano) de altíssima velocidade para execução em processadores comuns (CPU) sem a necessidade de hardware gráfico dedicado.
* **OpenCV (`cv2`):** Biblioteca base para processamento matricial e manipulação de arquivos de imagem.
* **Groq SDK & LPU Hardware:** Cliente de conexão com os servidores da Groq, que utilizam chips de processamento de linguagem (Language Processing Units) para devolver análises complexas em milissegundos.

---

## 📂 Estrutura Final do Repositório

```text
├── imagens_entrada/     # Imagens originais (matéria-prima) prontas para análise
├── resultados/          # Imagens anotadas e os relatórios em texto gerados pela LLM
├── .env                 # Cofre de segurança contendo a GROQ_API_KEY
├── .gitignore           # Bloqueio de upload de variáveis sensíveis
├── recom.py             # Módulo da Fase 1 (Visão Computacional Local)
└── recom_groq.py        # Módulo da Fase 2 (Pipeline Integrado Edge-to-Cloud)