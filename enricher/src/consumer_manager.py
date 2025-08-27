from kafka_configuration import consumer


class ConsumerManager:

    def __init__(self, topic1='raw_tweets_antisemitic', topic2='raw_tweets_not_antisemitic'):
        self.events = consumer(topic1, topic2)

    def get_massages_from_kafka(self):
        for messages in self.events:
            print(messages.value)


c = ConsumerManager()
c.get_massages_from_kafka()



