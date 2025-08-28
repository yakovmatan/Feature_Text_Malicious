from utils.kafka_configuration import consumer
from persister.src.mongodb_connection import DbConnection


class ConsumerManager:

    def __init__(self, topic1='enriched_preprocessed_tweets_antisemitic', topic2='enriched_preprocessed_tweets_not_antisemitic', collection1='tweets_antisemitic', collection2="tweets_not_antisemitic"):
        self.events = consumer(topic1, topic2)
        self.connection = DbConnection()
        self.collection1 = self.connection.db[collection1]
        self.collection2 = self.connection.db[collection2]


    def consumer_to_mongodb(self):
        for messages in self.events:
            if messages.topic == "enriched_preprocessed_tweets_antisemitic":
                self.collection1.insert_one(messages.value)
            else:
                self.collection2.insert_one(messages.value)