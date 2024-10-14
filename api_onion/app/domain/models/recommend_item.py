from dataclasses import dataclass

@dataclass
class RecommendItem:
    """
    推薦アイテムのデータモデル。
    """
    item_id: str
    item_name: str