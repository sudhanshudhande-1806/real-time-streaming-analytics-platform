import logging

logging.basicConfig(
    filename='../logs/streaming.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

logging.info("Streaming Pipeline Started")