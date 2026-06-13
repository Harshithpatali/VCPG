from fastapi import FastAPI

from backend.routes.prompt_routes import router

app = FastAPI(
    title="VCPG API",
    version="1.0.0",
    description="Vibe Coding Prompt Generator API"
)

app.include_router(router)


@app.get("/")
async def root():
    return {
        "message": "VCPG Backend Running"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }