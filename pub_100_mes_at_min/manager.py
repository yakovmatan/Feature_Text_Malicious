from fetcher import Fetcher
from configuration.kafka-configuration import send_event
from data import Data
import time
import os

class Manager:
    def __init__(self):
        self.connection = Fetcher()
        self.data = Data(connection=self.connection)


    def publish_every_minute(self):
        while True:
            documents = self.data.get_100_memesege()
            self.data.split_data_per_category(documents)
            send_event('raw_tweets_antisemitic', self.data.antisemitic)
            send_event('raw_tweets_not_antisemitic', self.data.not_antisemitic)
            time.sleep(60)


