from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'customer-events',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Monitoring Started...")

for message in consumer:

    print("Received:", message.value)