from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import health, ai

app = FastAPI(
    title="AI Money Mentor API",
    description="Financial Planning & AI Advisor Backend",
    version="1.0.0"
)

# 🔹 Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 Include routes
app.include_router(health.router)
app.include_router(ai.router)
# app.include_router(ai.router)
# 🔹 Root endpoint
@app.get("/")
def root():
    return {"message": "AI Money Mentor Backend Running 🚀"}