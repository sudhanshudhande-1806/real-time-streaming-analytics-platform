CREATE TABLE streaming_events (

    id SERIAL PRIMARY KEY,

    product VARCHAR(100),

    amount INT,

    city VARCHAR(100),

    created_at TIMESTAMP
);