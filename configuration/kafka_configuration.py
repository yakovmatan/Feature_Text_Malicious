import json
from kafka import KafkaProducer
from kafka import KafkaConsumer
import os

kafka_broker = os.getenv('KAFKA_BROKER', 'localhost:9092')


def produce():
    return KafkaProducer(bootstrap_servers=[kafka_broker],
                         value_serializer=lambda x:
                         json.dumps(x).encode('utf-8'))

def send_event(topic, event):
    producer = produce()
    producer.send(topic, event)
    producer.flush()


def consumer(topic, group):
    try:
        events = KafkaConsumer(topic,
                               group_id=group,
                               value_deserializer=lambda m: json.loads(m.decode('ascii')),
                               bootstrap_servers=[kafka_broker])
        return events
    except:
        return 'consume eror'

