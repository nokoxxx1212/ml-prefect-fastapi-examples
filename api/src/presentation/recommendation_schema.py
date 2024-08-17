from pydantic import BaseModel
from typing import List

class RecommendationResponse(BaseModel):
    recommendations: List[str]
