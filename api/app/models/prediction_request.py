from pydantic import BaseModel
from enum import Enum

class UserType(str, Enum):
  LOGGED = "Logged"
  NON_LOGGED = "Non-Logged"

class PredictionRequest(BaseModel):
  user: str
  userType: UserType