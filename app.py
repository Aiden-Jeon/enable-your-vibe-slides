from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

BASE_DIR = Path(__file__).parent

app.mount("/sections", StaticFiles(directory=BASE_DIR / "sections", html=True), name="sections")
app.mount("/shared", StaticFiles(directory=BASE_DIR / "shared"), name="shared")

@app.get("/")
async def root():
    return FileResponse(BASE_DIR / "index.html")
