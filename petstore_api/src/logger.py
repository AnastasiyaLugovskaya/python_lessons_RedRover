import logging
import os
from logging.handlers import RotatingFileHandler
from petstore_api.functions import get_current_path


def create_logs():
    file_name = "logs.log"
    log_dir = get_current_path("logs")

    if not os.path.exists(log_dir):
        os.mkdir(log_dir)

    file_path = os.path.join(log_dir, file_name)
    return file_path


def get_logger(name: str):
    log_file = create_logs()
    max_bytes = 1024 * 1024 * 1
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        fmt='%(levelname)s | %(asctime)s | %(message)s | test_name: %(name)s',
        datefmt='%Y-%m-%d %H:%M:%S'
        )
    handler = logging.handlers.RotatingFileHandler(
        filename=log_file,
        encoding='utf-8',
        maxBytes=max_bytes,
        backupCount=10
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
