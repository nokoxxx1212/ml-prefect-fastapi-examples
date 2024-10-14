from abc import ABC, abstractmethod
from typing import List
from app.infrastructure.repositories.recommend_item_repository import RecommendItemRepository
from app.infrastructure.clients.bigtable import BigTableClient
from app.infrastructure.clients.client_interface import IClient

class IRecommender(ABC):
    """
    推薦アイテムを推定するためのインターフェース。
    """
    @abstractmethod
    async def recommend(self, user_id: str) -> List[str]:
        pass

class StaticItemRecommender(IRecommender):
    """
    固定の推薦アイテムを返す具体的なクラス。
    """
    async def recommend(self, user_id: str) -> List[str]:
        # 固定の推薦アイテムを返す
        return ["itemS1", "itemS2", "itemS3"]

class ItemRecommender(IRecommender):
    def __init__(self, client: IClient):
        self.repository = RecommendItemRepository(client)

    async def recommend(self, user_id: str):
        return self.repository.get_recommendations(user_id)