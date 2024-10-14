from fastapi import FastAPI, Depends, HTTPException
from app.application.recommend_service import RecommendService
from app.domain.recommenders import IRecommender, StaticItemRecommender

async def lifespan(app: FastAPI):
    # アプリケーションの起動時に実行される処理をここに記述できます
    pass

app = FastAPI(lifespan=lifespan)

@app.get("/recommendations")
async def get_recommendations(user_id: str, recommender: IRecommender = Depends(StaticItemRecommender)):
    """
    ユーザーIDに基づいて推薦アイテムを取得するエンドポイント。
    """
    try:
        recommendations = await recommender.recommend(user_id)
        return {"recommendations": recommendations}
    except Exception as e:
        # 推薦アイテムの取得に失敗した場合のエラーハンドリング
        raise HTTPException(status_code=500, detail=str(e))