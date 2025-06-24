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
@app.post('/inference')
def predict(data: ModelInput):
    if model is None:
        return {'o modelo nao se enconta ou nao foi reconhecido'}
    try:
        input = data.model_dump()
        data_f = pd.DataFrame([input])
        
        #input_array = np.array([[data.credit_score, data.age, data.country, data.gender, data.tenure, data.balance,
                                #data.products_number, data.credit_card, data.active_member, data.estimated_salary, data.level_score]])
        predict = model.predict(data_f)
        return {f'prediçao: {int(predict[0])}'}
    except Exception as e:
        return {f'ocorreu um erro :{str(e)}'}
    