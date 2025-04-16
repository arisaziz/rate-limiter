FROM python:3.13-slim

WORKDIR /app

COPY app.py ./app.py
COPY requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]