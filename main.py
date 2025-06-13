from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {'siga a minha conta no tiktok'}