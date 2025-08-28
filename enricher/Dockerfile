FROM python:3.10-slim

WORKDIR /app

COPY enricher/requirements.txt .

RUN pip install -r requirements.txt

ENV NLTK_DATA=/usr/local/share/nltk_data
RUN python -m nltk.downloader -d /usr/local/share/nltk_data vader_lexicon

COPY utils /app/utils
COPY enricher/src /app/enricher/src

CMD ["python", "-m" , "enricher.src.main"]