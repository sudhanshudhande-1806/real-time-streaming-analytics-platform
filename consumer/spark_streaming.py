from kafka import KafkaConsumer
import json
import psycopg2
import logging

logging.basicConfig(
    filename='logs/pipeline.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

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

logging.info("Consumer Started")

for message in consumer:

    try:

        data = message.value

        print("Received:", data)

        logging.info(f"Received Event: {data}")

        if data['amount'] <= 0:

            logging.warning(
                f"Invalid Amount: {data}"
            )

            continue

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

        logging.info("Inserted into PostgreSQL")

    except Exception as e:

        logging.error(f"Error: {str(e)}")

        print("Error:", e)