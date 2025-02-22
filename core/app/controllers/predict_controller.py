from fastapi import APIRouter
from app.models.prediction_request import PredictionRequest
from app.services.predict import model_predict

router = APIRouter(prefix="/api", tags=["Predicts"])

@router.post("/predict")
async def predict(request: PredictionRequest):
  return model_predict(request)
