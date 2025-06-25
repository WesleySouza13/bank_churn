## **Bank Churn MLops: FastAPI + Docker + Render Cloud**
![capachurn2](https://github.com/user-attachments/assets/64f585e9-246f-4147-8c13-59853454e316)

Esse projeto foi desenvolvido afim de prever evasão (churn) em um ambiente bancário. A solução foi desenvolvida com o foco em aplicação de práticas de MLOps, garantindo reprodutibilidade, escalabilidade e facilidade de manutenção ao longo do ciclo de vida do modelo.

A proposta contempla todas as etapas essenciais de um pipeline moderno de machine learning orientado a produção:

- Preparação de dados: coleta, limpeza e transformação.

- Desenvolvimento e validação do modelo com abordagem modular.

- Serialização com joblib. 

- Deploy da API com FastAPI, tornando o modelo acessível via HTTP.

- Containerização com Docker, permitindo portabilidade e integração com pipelines de CI/CD.

- Automatização com scripts e pre-commit hooks, seguindo boas práticas de versionamento e padronização.

## Estrutura do projeto 

.
├── data/                             # Conjunto de dados (ex: Bank Customer Churn)
├── model/
│   ├── predict.py                    # Código para realizar predições
│   └── train.py                      # Código para treinar o modelo
├── notebook/
│   └── jupyter_notebook.ipynb       # Análises exploratórias e experimentos
├── venv/                             # Ambiente virtual Python
├── main.py                           # Arquivo principal que roda a API
├── modelo_gradientBoost.pkl         # Modelo treinado salvo
├── requirements.txt                  # Dependências do projeto
├── dockerfile                        # Dockerfile para containerização
├── install.sh                        # Script de instalação
├── .dockerignore
├── .gitignore
├── .pre-commit-config.yaml
└── README.md                         # Este arquivo
                   
