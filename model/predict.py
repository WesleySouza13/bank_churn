import json 
import requests

url = 'https://bank-churn-tiql.onrender.com'

response = requests.get(url=url)
if response.status_code == 200:
    print(response.text)
else:
    print('deu errado ')
    
url_pred = 'https://bank-churn-tiql.onrender.com/predict'
data = {
    "credit_score": 710,
    "country": "Italy",
    "gender": "Male",
    "age": 39,
    "tenure": 4,
    "balance": 34000.0,
    "products_number": 3,
    "credit_card": 0,
    "active_member": 1,
    "estimated_salary": 72000.0,
    "level_score": "medio"
}
data_json = json.dumps(data)
def inference(data):
    response_inference = requests.post(url=url_pred, data=data)
    if response_inference.status_code == 200:
        return response_inference.text
    else:
        print(f'erro: {response_inference.status_code} e {response_inference.text}')

# testando api 
teste = inference(data=data_json)
print(teste)
    
