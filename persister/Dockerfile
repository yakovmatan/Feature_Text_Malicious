FROM python:3.10-slim

WORKDIR /app

COPY persister/requirements.txt .

RUN pip install -r requirements.txt

COPY utils /app/utils
COPY persister/src /app/persister/src

CMD ["python", "-m", "persister.src.main"]