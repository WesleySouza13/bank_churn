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
                   
