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
        self.document["weapons_detected"] = []
        for w in weapons:
            if w in words:
                self.document["weapons_detected"].append(w)
        if not self.document["weapons_detected"]:
            self.document["weapons_detected"] = ""

        return self




