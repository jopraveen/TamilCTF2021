FROM python:latest

WORKDIR /app
COPY . .

EXPOSE 5002

RUN pip install -r requirements.txt 

ENTRYPOINT ["python", "app.py"]
