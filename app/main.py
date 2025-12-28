from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.routes import router
from app.config import Settings

app = FastAPI(
    title=Settings.APP_NAME,
    version=Settings.VERSION
)

@app.get("/", include_in_schema=False)
def redirect_to_docs():
    return RedirectResponse(url="/docs")

app.include_router(router)
