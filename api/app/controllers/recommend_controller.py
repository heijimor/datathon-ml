from fastapi import APIRouter
from app.models.prediction_request import PredictionRequest
from app.services.recommend import recommend

router = APIRouter(prefix="/api", tags=["Recommendations"])

@router.get("/recommend/{user_id}/type/{user_type}")
async def recommend_articles(user_id: str, user_type: str, top_n: int = 6):
  recommendations = recommend(user_id, user_type, top_n)
  if not recommendations:
    raise HTTPException(status_code=404, detail="Nenhuma recomendação encontrada.")
  return recommendations
