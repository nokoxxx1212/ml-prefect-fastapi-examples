from src.domain.user import User
from src.infrastructure.bigtable_repository import BigTableRepository

class RecommendationService:
    def __init__(self, repository: BigTableRepository):
        self.repository = repository

    def get_recommendations(self, user: User):
        # BigTableからユーザーに対する推薦結果を取得
        return self.repository.fetch_recommendations(user.user_id)
