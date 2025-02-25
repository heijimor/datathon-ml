from fastapi import APIRouter
from app.models.prediction_request import PredictionRequest
from app.services.recommend import model_recommend

router = APIRouter(prefix="/api", tags=["Recommendations"])

@router.get("/recommend/{user_id}")
async def recommend_articles(user_id: str, top_n: int = 5):
  return model_recommend(user_id)
