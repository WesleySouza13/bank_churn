# syntax=docker/dockerfile:1

FROM python:3.11.9

WORKDIR /appML

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt


COPY . . 
EXPOSE 10000
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
