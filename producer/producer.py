from kafka import KafkaConsumer
import json
import psycopg2

connection = psycopg2.connect(
    host="localhost",
    port="5433",
    database="streaming_db",
    user="admin",
    password="06041977"
)

cursor = connection.cursor()

consumer = KafkaConsumer(
    'customer-events',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Kafka Consumer Started...")

for message in consumer:

    data = message.value

    print("Received:", data)

    cursor.execute(
        """
        INSERT INTO streaming_events
        (product, amount, city, created_at)

        VALUES (%s, %s, %s, %s)
        """,
        (
            data['product'],
            data['amount'],
            data['city'],
            data['created_at']
        )
    )

    connection.commit()

    print("Inserted into PostgreSQL")