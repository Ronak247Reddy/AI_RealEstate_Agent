
import logging

def log(message):
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
    logging.info(message)
    