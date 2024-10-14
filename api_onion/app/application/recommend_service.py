from app.domain.recommenders import IRecommender

class RecommendService:
    """
    推薦アイテムを取得するためのサービスクラス。
    ドメイン層のビジネスロジックを呼び出す。
    """
    def __init__(self, recommender: IRecommender):
        self.recommender = recommender

    async def get_recommendations(self, user_id: str):
        # ドメイン層のロジックを使用して推薦アイテムを取得
        return await self.recommender.recommend(user_id)