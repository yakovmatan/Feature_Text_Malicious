import re
from datetime import datetime

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


class Enricher:

    def __init__(self):
        nltk.data.find("sentiment/vader_lexicon.zip")
        self.document = None

    def receiving_document(self,document):
        self.document = document

    def sentiment_of_text(self, text):
        score = SentimentIntensityAnalyzer().polarity_scores(text)
        if score['compound'] >= 0.5:
            self.document["sentiment"] = 'positive'
        elif score['compound'] >= -0.49:
            self.document["sentiment"] =  "neutral"
        else:
            self.document["sentiment"] = "negative"

        return self

    def weapon_in_text(self, text, weapons: list):
        words = text.split()
        detected = [w for w in weapons if w in words]
        self.document["weapons_detected"] = detected if detected else ""

        return self

    def add_latest_data(self, text):
        matches = re.findall(r"\b\d{4}-\d{2}-\d{2}\b", text)

        if matches:
            dates = [datetime.strptime(m, "%Y-%m-%d") for m in matches]
            latest = max(dates)
            self.document["relevant_timestamp"] = latest.strftime("%Y-%m-%d")
        else:
            self.document["relevant_timestamp"] = ""

        return self




