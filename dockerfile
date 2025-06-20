# syntax=docker/dockerfile:1

FROM python:3.11.9

WORKDIR /appML

copy requirements.txt requirements.txt

RUN pip install -r requirements.txt


copy . . 

CMD ["python", "-m","uvicorn", "main:app", "--reload", "--port", "8080"]