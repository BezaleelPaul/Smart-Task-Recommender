from fastapi import APIRouter
from app.models import UserState, TaskRecommendation
from app.recommender import recommend

router = APIRouter()

@router.post("/recommend", response_model=TaskRecommendation)
def get_recommendation(state: UserState):
    return recommend(state)

@router.get("/health")
def health_check():
    return {"status": "ok"}
