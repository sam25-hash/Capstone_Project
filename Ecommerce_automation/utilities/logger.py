import logging
from logging import handlers
from pathlib import Path

LOG_FILE = Path("logs/test.log")
LOG_FILE.parent.mkdir(exist_ok=True)


def get_logger(name="FrameworkLogger"):
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG)

    file_handler = handlers.RotatingFileHandler(
        LOG_FILE, maxBytes=5000000, backupCount=3
    )
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(fmt)
    console_handler.setFormatter(fmt)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
