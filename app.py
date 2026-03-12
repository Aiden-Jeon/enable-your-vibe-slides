import os
from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

BASE_DIR = Path(__file__).parent


@app.get("/api/config")
async def config():
    return {"workspace_url": os.environ.get("DATABRICKS_HOST", "")}


app.mount("/sections", StaticFiles(directory=BASE_DIR / "sections", html=True), name="sections")
app.mount("/shared", StaticFiles(directory=BASE_DIR / "shared"), name="shared")

@app.get("/favicon.svg")
async def favicon():
    return FileResponse(BASE_DIR / "favicon.svg", media_type="image/svg+xml")


@app.get("/")
async def root():
    return FileResponse(BASE_DIR / "index.html")
