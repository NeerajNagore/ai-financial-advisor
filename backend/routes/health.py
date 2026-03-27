from fastapi import APIRouter, HTTPException
from backend.models.user_model import UserFinancialData
from backend.services.finance_engine import calculate_health_score

router = APIRouter(prefix="/api", tags=["Health"])

@router.post("/health-score")
def get_health_score(user_data: UserFinancialData):
    try:
        result = calculate_health_score(user_data)
        return {
            "status": "success",
            "data": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))