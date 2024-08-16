import logging
import yaml
import logging.config

def get_logger(name: str) -> logging.Logger:
    # 絶対パスでログ設定ファイルを読み込む
    with open('ml_pipeline/config/logging_config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    logging.config.dictConfig(config)
    return logging.getLogger(name)