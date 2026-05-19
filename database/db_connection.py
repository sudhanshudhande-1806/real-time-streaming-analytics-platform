import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="streaming_db",
    user="admin",
    password="admin"
)

print("PostgreSQL Connected Successfully")