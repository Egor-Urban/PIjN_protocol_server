import logging
import os
from datetime import datetime
from concurrent_log_handler import ConcurrentRotatingFileHandler
from colorlog import ColoredFormatter



LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs")
os.makedirs(LOG_DIR, exist_ok=True)

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

log_filename = os.path.join(LOG_DIR, datetime.now().strftime("%Y-%m-%d") + ".log")

log = logging.getLogger("pijn_protocol")
log.setLevel(logging.INFO)



class RelativePathFormatter(logging.Formatter):
    def format(self, record):
        try:
            record.relpath = os.path.relpath(record.pathname, PROJECT_ROOT)
        except Exception:
            record.relpath = record.pathname
        return super().format(record)



file_handler = ConcurrentRotatingFileHandler(
    log_filename,
    maxBytes=10*1024*1024,
    backupCount=7,
    encoding="utf-8"
)
file_handler.setLevel(logging.INFO)


file_formatter = RelativePathFormatter(
    "[%(asctime)s][%(relpath)s:%(funcName)s][%(levelname)s] %(message)s",
    datefmt="%d.%m.%Y %H:%M"
)
file_handler.setFormatter(file_formatter)


console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)


color_formatter = ColoredFormatter(
    "%(log_color)s[%(asctime)s][%(relpath)s:%(funcName)s][%(levelname)s] %(message)s",
    datefmt="%d.%m.%Y %H:%M",
    log_colors={
        "DEBUG":    "white",
        "INFO":     "green",
        "WARNING":  "yellow",
        "ERROR":    "red",
        "CRITICAL": "bold_red",
    }
)
console_handler.setFormatter(color_formatter)


log.addHandler(file_handler)
log.addHandler(console_handler)


django_logger = logging.getLogger("django")
django_logger.handlers = [file_handler, console_handler]
django_logger.setLevel(logging.INFO)
