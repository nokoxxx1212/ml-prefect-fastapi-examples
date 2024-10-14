from fastapi import FastAPI, Depends, HTTPException
from app.application.recommend_service import RecommendService
from app.domain.recommenders import IRecommender
from app.domain.recommenders import StaticItemRecommender
from app.domain.recommenders import BigTableRecommender
from app.infrastructure.clients.bigtable import BigTableClient

async def lifespan(app: FastAPI):
    # アプリケーションの起動時に実行される処理をここに記述できます
    pass

app = FastAPI(lifespan=lifespan)

# 依存性注入
# def get_recommend_service(recommender: IRecommender = Depends(StaticItemRecommender)):
#     return RecommendService(recommender)
def get_recommend_service(recommender: IRecommender = Depends(lambda: BigTableRecommender(BigTableClient()))):
    return RecommendService(recommender)

@app.get("/recommendations")
async def get_recommendations(user_id: str, service: RecommendService = Depends(get_recommend_service)):
    """
    ユーザーIDに基づいて推薦アイテムを取得するエンドポイント。
    """
    try:
        recommendations = await service.get_recommendations(user_id)
        return {"recommendations": recommendations}
    except Exception as e:
        # 推薦アイテムの取得に失敗した場合のエラーハンドリング
        raise HTTPException(status_code=500, detail=str(e))