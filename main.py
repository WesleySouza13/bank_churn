from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd

app = FastAPI()
model = joblib.load('modelo_gradientBoosting.pkl')
print(type(model))
class ModelInput(BaseModel):
    credit_score: int
    country:str
    gender:str
    age:int
    tenure:int
    balance:float
    products_number:int
    credit_card:int
    active_member:int
    estimated_salary:float
    level_score: str
@app.get('/')
def home():
    
    return {'api para previsao de churn - modelo de gradientBoosting. Criado por Wesley Matos no dia 20/06/2025'}
@app.post('/predict')
def predict(data: ModelInput):
    if model is None:
        return {'o modelo nao se enconta ou nao foi reconhecido'}
    try:
        input_data = data.model_dump()
        data_f = pd.DataFrame([input_data])
        predict = model.predict(data_f)
        pred_proba = model.predict_proba(data_f)[:,1]
        return {f'prediçao: {int(predict[0])} e probabilidade de {float(pred_proba[0])*100:.2f}% para churn'}
    except Exception as e:
        return {f'ocorreu um erro :{str(e)}'}
    