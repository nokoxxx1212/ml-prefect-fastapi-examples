from fastapi import FastAPI, HTTPException
from src.application.recommendation_service import RecommendationService
from src.domain.user import User
from src.infrastructure.bigtable_repository import BigTableRepository
from src.presentation.recommendation_schema import RecommendationResponse
from src.infrastructure.logger import get_logger

app = FastAPI(title="Recommendation API", version="1.0.0", debug=True)
logger = get_logger(__name__)

# Recommendation Serviceのインスタンスを生成
repository = BigTableRepository()
recommendation_service = RecommendationService(repository)

@app.get("/recommendations", response_model=RecommendationResponse)
async def get_recommendations(user_id: str):
    user = User(user_id=user_id)
    try:
        recommendations = recommendation_service.get_recommendations(user)
        logger.info(f"Recommendations retrieved for user_id: {user_id}")
        return RecommendationResponse(recommendations=recommendations)
    except Exception as e:
        logger.error(f"Error retrieving recommendations: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
