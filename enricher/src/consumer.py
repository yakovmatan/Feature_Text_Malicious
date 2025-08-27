from kafka_configuration import consumer


class Consumer:

    def __init__(self, topic1='raw_tweets_antisemitic', topic2='raw_tweets_not_antisemitic'):
        self.events = consumer(topic1, topic2)

    def print_events(self):
        for messages in self.events:
            print(messages.topic)

c = Consumer()
c.print_events()



