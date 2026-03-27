from pydantic import BaseModel, Field, validator
from typing import Optional

class UserFinancialData(BaseModel):
    age: int = Field(..., gt=0, lt=100)
    income: float = Field(..., gt=0)
    expenses: float = Field(..., gt=0)
    savings: float = Field(..., ge=0)
    loan: float = Field(default=0, ge=0)
    insurance: Optional[bool] = False

    @validator("expenses")
    def expenses_less_than_income(cls, v, values):
        if "income" in values and v > values["income"]:
            raise ValueError("Expenses cannot exceed income")
        return v