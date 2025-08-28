from enricher import Enricher
from read_files import ReadFile
from kafka_configuration import consumer, produce, send_event


class ConsumerManager:

    def __init__(self, topic1='preprocessed_tweets_antisemitic', topic2='preprocessed_tweets_not_antisemitic'):
        self.events = consumer(topic1, topic2)
        self.enricher = Enricher()
        self.weapons = ReadFile(path='../data/weapon_list.txt').read_file().split('\n')
        self.producer = produce()


    def publish_messages(self):
        for messages in self.events:
            self.enricher.receiving_document(messages.value)
            new_document = (
                self.enricher
                .sentiment_of_text(messages.value["text"])
                .add_latest_data(messages.value["text"])
                .weapon_in_text(messages.value["text"], self.weapons)
                .document
            )
            if messages.topic == "preprocessed_tweets_antisemitic":
                send_event(self.producer, "enriched_preprocessed_tweets_antisemitic", new_document)
            else:
                send_event(self.producer, "enriched_preprocessed_not_tweets_antisemitic", new_document)