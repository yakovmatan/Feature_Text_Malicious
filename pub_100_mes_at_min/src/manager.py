from fetcher import Fetcher
from kafka_configuration import produce, send_event
from data import Data


class Manager:
    def __init__(self):
        self.connection = Fetcher()
        self.data = Data(connection=self.connection)
        self.producer = produce()


    def publish_messages(self):
        documents = self.data.get_100_messages()
        for document in documents:
            if document["Antisemitic"]:
                document["CreateDate"] = document["CreateDate"].isoformat()
                send_event(self.producer,'raw_tweets_antisemitic', document)
            else:
                document["CreateDate"] = document["CreateDate"].isoformat()
                send_event(self.producer, 'raw_tweets_not_antisemitic', document)