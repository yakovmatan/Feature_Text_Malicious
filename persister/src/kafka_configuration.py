import json
from kafka import KafkaProducer
from kafka import KafkaConsumer
import os

kafka_broker = os.getenv('KAFKA_BROKER', 'localhost:9092')



def consumer(topic1, topic2):
    try:
        events = KafkaConsumer(topic1, topic2,
                               group_id='my_group',
                               value_deserializer=lambda m: json.loads(m.decode('ascii')),
                               bootstrap_servers=[kafka_broker])
        return events
    except Exception as e:
        return {'consume error': e}

