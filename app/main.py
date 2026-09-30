from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes import router

app = FastAPI(
    title="ComicCraft AI"
)

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

app.mount(
    "/generated",
    StaticFiles(directory="generated"),
    name="generated"
)

app.include_router(router)


@app.get("/health")
async def health():
    return {
        "status": "ok"
    }