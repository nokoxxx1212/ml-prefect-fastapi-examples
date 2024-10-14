from app.infrastructure.clients.client_interface import IClient

class RecommendItemRepository:
    """
    推薦アイテムを取得するためのリポジトリクラス。
    """
    def __init__(self, client: IClient):
        self.client = client

    def get_recommendations(self, user_id: str):
        return self.client.get_data(user_id)