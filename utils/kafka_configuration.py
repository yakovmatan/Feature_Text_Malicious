import json
from kafka import KafkaProducer
from kafka import KafkaConsumer
import os

kafka_broker = os.getenv('KAFKA_BROKER', 'kafka-broker:9092')


def consumer(topic1, topic2):
    try:
        events = KafkaConsumer(topic1, topic2,
                               group_id='my_group',
                               value_deserializer=lambda m: json.loads(m.decode('ascii')),
                               bootstrap_servers=[kafka_broker])
        return events
    except Exception as e:
        raise RuntimeError(f"consumer creation failed: {e}")


def produce():
    try:
        producer = KafkaProducer(bootstrap_servers=[kafka_broker],
                             value_serializer=lambda x:
                             json.dumps(x).encode('utf-8'))
        return producer
    except Exception as e:
        raise RuntimeError(f"producer creation failed: {e}")

def send_event(producer, topic, event):
    producer.send(topic, event)
    producer.flush()

