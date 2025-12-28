from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Smart Task Recommender")
app.include_router(router)

