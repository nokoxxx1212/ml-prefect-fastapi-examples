from abc import ABC, abstractmethod
from typing import List

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
        return ["item1", "item2", "item3"]