from pydantic import BaseModel, Field

class UserState(BaseModel):
    mood: int = Field(..., ge=1, le=5)
    energy: int = Field(..., ge=1, le=5)
    stress: int = Field(..., ge=1, le=5)
    available_time: int = Field(..., gt=0)

class TaskRecommendation(BaseModel):
    task: str
    reason: str
