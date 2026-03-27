from fastapi import APIRouter
from backend.services.ai_engine import generate_financial_advice
from pydantic import BaseModel
# from backend.services.ai_engine import generate_financial_advice

from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.ai_engine import generate_financial_advice

router = APIRouter()

class UserData(BaseModel):
    age: int
    income: float
    expenses: float
    savings: float
    loan: float
    insurance: bool

@router.post("/api/ai-advice")
def get_ai_advice(data: UserData):   # ✅ automatically body
    try:
        result = generate_financial_advice(data.dict())
        return result
    except Exception as e:
        return {
            "error": str(e),
            "score": {"score": 0},
            "advice": "Something went wrong while generating advice."
        }