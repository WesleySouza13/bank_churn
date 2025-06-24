# syntax=docker/dockerfile:1

FROM python:3.11.9

WORKDIR /appML

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt


COPY . . 
EXPOSE 8000
CMD ["python", "-m","uvicorn", "main:app", "--reload"]