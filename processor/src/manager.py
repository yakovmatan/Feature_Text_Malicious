from utils.kafka_configuration import *
from utils.text_processing import TextProcessing

class Manager:
    def __init__(self):
        self.original_antisemitic_topic = 'raw_tweets_antisemitic'
        self.original_not_antisemitic_topic = 'raw_tweets_not_antisemitic'
        self.new_antisemitic_topic = 'preprocessed_tweets_antisemitic'
        self.new_not_antisemitic_topic = 'preprocessed_tweets_not_antisemitic'
        self.producer = produce()



    def get_document_from_kafka_processing_and_publish_processed_document(self):
        events = consumer(self.original_antisemitic_topic, self.original_not_antisemitic_topic)
        for messages in events:
            document = messages.value
            document = self.processing_document(document)
            self.publish_messages(document, messages.topic)

    def processing_document(self, document):
        text_processing = TextProcessing(document['text'])
        text_processing.cleaning_text()
        document['clean_text'] = text_processing.clean_text
        return document



    def publish_messages(self,document, topic):
        if topic == 'raw_tweets_antisemitic':
            send_event( self.producer, self.new_antisemitic_topic, document)
        else:
            send_event(self.producer, self.new_not_antisemitic_topic, document)


