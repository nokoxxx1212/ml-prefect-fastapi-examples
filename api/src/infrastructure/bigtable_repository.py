from src.infrastructure.logger import get_logger

logger = get_logger(__name__)

class BigTableRepository:
    def fetch_recommendations(self, user_id: str):
        # BigTableにアクセスするコードをここに記載
        # 現在は固定のレスポンスを返すようにしています
        logger.info(f"Fetching recommendations for user_id: {user_id}")
        return ["item1", "item2", "item3"]
