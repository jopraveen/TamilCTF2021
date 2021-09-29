FROM python:latest

WORKDIR /app
COPY . .

EXPOSE 5000

RUN pip install -r requirements.txt 

ENTRYPOINT ["python", "app.py"]
