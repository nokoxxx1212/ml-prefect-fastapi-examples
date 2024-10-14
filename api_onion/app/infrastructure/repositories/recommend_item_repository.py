from app.infra.clients.bigtable import BigTableClient

class RecommendItemRepository:
    """
    推薦アイテムを取得するためのリポジトリクラス。
    BigTableクライアントを使用してデータを取得。
    """
    def __init__(self, client: BigTableClient):
        self.client = client

    def get_recommendations(self, user_id: str):
        # BigTableからデータを取得する処理を呼び出す
        return self.client.get_data(user_id)