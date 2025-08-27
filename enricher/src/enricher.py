import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


class Enricher:

    def __init__(self):
        nltk.data.find("sentiment/vader_lexicon.zip")
        self.document = None

    def receiving_document(self,document):
        self.document = document

    def sentiment_of_text(self):
        score = SentimentIntensityAnalyzer().polarity_scores(self.document)
        if score['compound'] >= 0.5:
            self.document["sentiment"] = 'positive'
        elif score['compound'] >= -0.49:
            self.document["sentiment"] =  "neutral"
        else:
            self.document["sentiment"] = "negative"

        return self



