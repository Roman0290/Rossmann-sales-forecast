import logging
from pathlib import Path

def setup_logger(name, log_file="eda.log", level=logging.INFO):
    """Setup logger for EDA"""
    Path("outputs/logs/").mkdir(parents=True, exist_ok=True)
    handler = logging.FileHandler(f"outputs/logs/{log_file}")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger
