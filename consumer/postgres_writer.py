def write_to_postgres(batch_df, batch_id):

    batch_df.write \
        .format("jdbc") \
        .option(
            "url",
            "jdbc:postgresql://localhost:5433/streaming_db"
        ) \
        .option("dbtable", "streaming_events") \
        .option("user", "admin") \
        .option("password", "06041977") \
        .option("driver", "org.postgresql.Driver") \
        .mode("append") \
        .save()

    print(f"Batch {batch_id} written successfully")