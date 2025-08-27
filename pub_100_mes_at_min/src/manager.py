from fetcher import Fetcher
from kafka_configuration import send_event
from data import Data



class Manager:
    def __init__(self):
        self.connection = Fetcher()
        self.data = Data(connection=self.connection)


    def publish_messages(self):
        documents = self.data.get_100_messages()
        for document in documents:
            if document["Antisemitic"]:
                document["_id"] = str(document["_id"])
                document["CreateDate"] = document["CreateDate"].isoformat()
                send_event('raw_tweets_antisemitic', document)
            else:
                document["_id"] = str(document["_id"])
                document["CreateDate"] = document["CreateDate"].isoformat()
                send_event('raw_tweets_not_antisemitic', document)