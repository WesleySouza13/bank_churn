## **Bank Churn MLops: FastAPI + Docker + Render Cloud** 🧑‍💻☁️
![capachurn2](https://github.com/user-attachments/assets/64f585e9-246f-4147-8c13-59853454e316)

Esse projeto foi desenvolvido afim de prever evasão (churn) em um ambiente bancário. A solução foi desenvolvida com o foco em aplicação de práticas de MLOps, garantindo reprodutibilidade, escalabilidade e facilidade de manutenção ao longo do ciclo de vida do modelo.

A proposta contempla todas as etapas essenciais de um pipeline moderno de machine learning orientado a produção:

- Preparação de dados: coleta, limpeza e transformação.

- Desenvolvimento e validação do modelo com abordagem modular.

- Serialização com joblib. 

- Deploy da API com FastAPI, tornando o modelo acessível via HTTP.

- Containerização com Docker, permitindo portabilidade e integração com pipelines de CI/CD.

- Automatização com scripts e pre-commit hooks, seguindo boas práticas de versionamento e padronização.

## Estrutura do projeto 🗂️

.
├── data/                            
├── model/                          
│   ├── train.py                    
│   └── predict.py                  
├── notebook/                        
│   └── jupyter_notebook.ipynb      
├── main.py                         
├── modelo_gradientBoost.pkl         
├── requirements.txt                 
├── install.sh                      
├── dockerfile                       
├── .dockerignore                    
├── .gitignore                      
├── .pre-commit-config.yaml          
├── README.md                        
└── venv/                            

## Tecnologias usadas

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Render](https://img.shields.io/badge/Render-%46E3B7.svg?style=for-the-badge&logo=render&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

## Métricas do modelo 

Primeiramente, foi realizado um estudo com diversos modelos de classificação. Em um primeiro momento, foram selecionados os três melhores modelos: Random Forest, LightGBM e Gradient Boosting.

Abaixo está a curva ROC AUC dos modelos: 

![image](https://github.com/user-attachments/assets/8128e8dd-6423-421b-8a43-ff3f3242fc85)

Abaixo estão as métricas principais de cada um:

| Modelo 
|(classe desbalanceada)       | Acurácia   | F1-Score   | Recall     | Precision | ROC AUC    |
| --------------------------- | ---------- | ---------- | ---------- | --------- | ---------- |
| **Random Forest**           | 0.7755     | 0.4869     | 0.5000     | 0.4744    | 0.6750     |
| **Gradient Boosting**       | 0.8495     | 0.5541     | 0.4390     | 0.7510    | **0.8694** |
| **LightGBM**                | **0.8540** | **0.5852** | **0.4836** | 0.7410    | 0.8617     |


Como estamos lidando com um problema de churn, o principal objetivo é identificar corretamente a maior quantidade possível de clientes que estão propensos a sair. Por esse motivo, foi dada prioridade à métrica de recall, que mede a capacidade do modelo em capturar os casos positivos.
Dessa forma, o modelo escolhido (por enquanto) para deploy foi o Gradient Boosting, por apresentar o melhor desempenho em recall entre os modelos avaliados.

## Tratamento de classes desbalanceadas

Para o tratamento do desbalanceamento de classes, foram realizados testes com diferentes estratégias, como RandomOversampling e RandomUndersampling.
Através desses experimentos, foi possível identificar que a técnica de RandomOversampling proporcionou as melhores métricas de desempenho para o modelo selecionado (Gradient Boosting), especialmente no que diz respeito ao recall e ao F1-Score.

Abaixo estão as métricas pós Oversampling: 

| Modelo                | Acurácia | F1-Score   | Recall     | Precision | ROC AUC |
| --------------------- | -------- | ---------- | ---------- | --------- | ------- |
| **Random Forest**     | 0.8515   | 0.6077     | 0.5399     | 0.6949    | 0.7379  |
| **Gradient Boosting** | 0.8055   | 0.6145     | **0.7277** | 0.5317    | 0.7771  |
| **LightGBM**          | 0.8225   | **0.6243** | 0.6925     | 0.5684    | 0.7751  |







                   
