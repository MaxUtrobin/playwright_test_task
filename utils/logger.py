import logging
import sys


def get_logger(name="api"):
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] %(message)s", "%H:%M:%S"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger
