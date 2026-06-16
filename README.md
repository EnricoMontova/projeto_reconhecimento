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

---

## 🚀 Fase 2: O Salto Cognitivo (Integração Edge-to-Cloud)

Para elevar o projeto ao patamar de **Sistemas Inteligentes**, a Fase 2 (`recom_groq.py`) introduziu uma camada de Inteligência Artificial Generativa. O pipeline deixou de ser apenas um extrator gráfico e passou a funcionar como um integrador cognitivo.

Nesta arquitetura atualizada, a telemetria visual coletada na borda (Edge) alimenta um modelo de linguagem na nuvem (Cloud) em tempo real:

1. **Extração de Telemetria Visual:** O sistema intercepta as propriedades do YOLOv8, extraindo o ID numérico, a tradução textual da classe e o índice estatístico de certeza de cada objeto.
2. **Contrato de Dados e Serialização (O Papel do JSON):** Dicionários criados pelo Python existem apenas na memória RAM local e não podem trafegar pela internet. Para viabilizar a comunicação com a nuvem, o sistema realiza a **serialização** (`json.dumps()`), convertendo os dados em texto estruturado. O formato JSON foi adotado estrategicamente por três motivos:
   * **Transporte Leve:** Transforma objetos complexos em texto puro para tráfego em rede sem latência.
   * **Universalidade:** Como padrão universal de APIs, garante que os servidores da Groq leiam a requisição independentemente da linguagem em que operam.
   * **Otimização de LLM:** O padrão estrito do JSON é nativamente reconhecido e otimizado no treinamento de modelos de linguagem, garantindo uma interpolação limpa no *prompt* e eliminando erros de interpretação por parte da IA.
3. **Inferência e Inteligência:** A requisição em texto é enviada à API da Groq para gerar relatórios com ações recomendadas baseadas no que foi detectado no ambiente físico.

---

## 🧠 Documentação de Prompts e Justificativa do Modelo

A interação com a Inteligência Artificial no projeto ocorre através de uma técnica estrita de Engenharia de Prompt, garantindo previsibilidade e formato corporativo.

### Estrutura dos Prompts Utilizados
* **System Prompt (O Comportamento Base):**
  > *"Você é um sistema inteligente especialista em análise de dados de sensores e automação industrial. Responda em tópicos claros e objetivos."*
  
  **Justificativa:** Define a persona como um "especialista em automação", forçando a IA a abandonar um tom genérico e adotar vocabulário técnico aplicável a ambientes industriais e *dashboards* de gestão.
  
* **User Prompt (A Injeção de Dados):**
  > *"Aqui estão os resultados de um sistema de Visão Computacional (YOLOv8)... Analise estes dados estruturados e forneça: 1. Um panorama geral... 2. Identificação de padrões ou anomalias... 3. Recomendações de ação... Dados extraídos: {payload_json}"*
  
  **Justificativa:** O envio do dicionário formatado (`payload_json`) garante que a LLM compreenda a hierarquia das detecções. As três diretrizes estruturam a resposta em um formato de "Relatório Executivo".

### Escolha da Infraestrutura (`llama-3.3-70b-versatile` via Groq)
* **Capacidade de Raciocínio (70B):** O Llama 70B possui a profundidade necessária para cruzar múltiplas variáveis logísticas e industriais com precisão.
* **Infraestrutura Cloud (LPUs):** Executar um modelo desse porte localmente é inviável. A Groq utiliza LPUs (Language Processing Units), permitindo que a requisição retorne a análise em milissegundos, viabilizando o monitoramento operacional ágil.
* **Controle de Entropia (`temperature=0.2`):** Reduz a aleatoriedade e criatividade do modelo. Em TI industrial, isso garante relatórios lógicos, determinísticos e estritamente amarrados aos dados da visão computacional, mitigando alucinações.

---

## 📊 Análise Crítica: Qualidade das Respostas em Casos Reais

Durante os testes com imagens de operações logísticas, manutenção de TI e salas de controle, o sistema demonstrou comportamentos importantes que validam a arquitetura e expõem oportunidades de melhoria.

### Pontos Fortes e Valor Gerado
* **Dedução de Contexto (Context Awareness):** A LLM cruzou a presença de "pessoas" e "caminhões" para deduzir ativamente cenários logísticos e sugerir protocolos de tráfego.
* **Compreensão de Infraestrutura de TI:** A IA mapeou com precisão salas de controle (identificando monitores, laptops e cadeiras) e sugeriu a verificação da manutenção de estações de trabalho e ergonomia.
* **Aproveitamento de Metadados Ocultos:** O sistema correlacionou o título dos arquivos gerados (ex: imagens nomeadas com tags de EPIs) com as detecções, gerando alertas de segurança do trabalho altamente precisos mesmo quando a visão não detectava a luva em si, provando o valor do tráfego JSON.

### Limitações e Gargalos (Crítica Técnica)
* **A Cegueira Herdada (Gargalo da Borda):** A nuvem é refém da borda. Se o modelo YOLO local falhar em enviar um objeto no JSON (falso negativo), a LLM será "cega" àquele risco.
* **Interpretação Estática da Confiança:** O relatório gera alertas sobre "confiança baixa (0.54)" supondo imagens borradas ou objetos ocultos. A LLM faz suposições inteligentes baseadas no dado estatístico, mas não "enxerga" o real motivo físico da baixa confiança.
* **Generalização de Lotes:** Quando o lote processado mistura imagens de contextos muito diferentes (ex: um avião, uma sala de TI e um pátio de caminhões simultaneamente), o relatório tenta criar recomendações generalistas. Em produção, o ideal é que a segregação do JSON ocorra por câmera/setor para gerar inteligência direcionada.

---

## 🛠️ Stack Tecnológico Consolidado

* **Python & python-dotenv:** Orquestração do fluxo de execução e isolamento seguro de credenciais (API Keys).
* **Ultralytics YOLOv8 (`yolov8n.pt`):** Motor de *Deep Learning* (versão Nano) local, leve e otimizado para CPU.
* **OpenCV (`cv2`):** Processamento matricial e manipulação de arquivos de imagem.
* **Groq SDK & LPU Hardware:** Conexão com os servidores em nuvem de alta velocidade para inferência LLM.

---

## 📂 Estrutura Final do Repositório

```text
├── imagens_entrada/     # Imagens originais (matéria-prima) prontas para análise
├── resultados/          # Imagens anotadas e os relatórios em texto gerados pela LLM
├── .env                 # Cofre de segurança contendo a GROQ_API_KEY
├── .gitignore           # Bloqueio de upload de variáveis sensíveis
├── recom.py             # Módulo da Fase 1 (Visão Computacional Local)
└── recom_groq.py        # Módulo da Fase 2 (Pipeline Integrado Edge-to-Cloud)