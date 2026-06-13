from fastapi import FastAPI

from backend.api.auth.router import router as auth_router

app = FastAPI(
    title="CleanCityAI"
)

app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "CleanCityAI Running"
    }