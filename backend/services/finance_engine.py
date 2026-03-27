from typing import Dict

def calculate_health_score(data) -> Dict:
    income = data.income
    expenses = data.expenses
    savings = data.savings
    loan = data.loan
    insurance = data.insurance

    score = 0
    breakdown = {}
    recommendations = []

    # 🔹 Emergency Fund
    if savings >= 6 * expenses:
        score += 20
        breakdown["emergency_fund"] = "Excellent"
    elif savings >= 3 * expenses:
        score += 10
        breakdown["emergency_fund"] = "Moderate"
        recommendations.append("Increase emergency fund to 6 months of expenses")
    else:
        breakdown["emergency_fund"] = "Poor"
        recommendations.append("Build emergency fund urgently")

    # 🔹 Debt Health
    debt_ratio = loan / income if income else 0
    if debt_ratio < 0.3:
        score += 20
        breakdown["debt"] = "Healthy"
    elif debt_ratio < 0.6:
        score += 10
        breakdown["debt"] = "Moderate"
        recommendations.append("Reduce debt burden")
    else:
        breakdown["debt"] = "High Risk"
        recommendations.append("High debt detected, prioritize repayment")

    # 🔹 Savings Rate
    savings_rate = (income - expenses) / income
    if savings_rate > 0.3:
        score += 20
        breakdown["savings_rate"] = "Strong"
    elif savings_rate > 0.15:
        score += 10
        breakdown["savings_rate"] = "Average"
        recommendations.append("Increase savings rate to at least 30%")
    else:
        breakdown["savings_rate"] = "Weak"
        recommendations.append("Your savings are too low")

    # 🔹 Insurance
    if insurance:
        score += 20
        breakdown["insurance"] = "Covered"
    else:
        breakdown["insurance"] = "Not Covered"
        recommendations.append("Get health/life insurance")

    # 🔹 Investment Potential
    if savings_rate > 0.2:
        score += 20
        breakdown["investment"] = "Good"
    else:
        breakdown["investment"] = "Needs Improvement"

    return {
        "score": score,
        "breakdown": breakdown,
        "recommendations": recommendations
    }