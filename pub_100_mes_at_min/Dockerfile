FROM python:3.10-slim

WORKDIR /app

COPY pub_100_mes_at_min/requirements.txt .

RUN pip install -r requirements.txt

COPY utils /app/utils
COPY pub_100_mes_at_min/src /app/pub_100_mes_at_min/src

CMD ["python", "-m", "pub_100_mes_at_min.src.main"]



