import logging
import logging.config
import yaml
import os

def get_logger(name: str) -> logging.Logger:
    with open("config/logging_config.yaml", 'r') as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    return logging.getLogger(name)
