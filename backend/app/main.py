from fastapi import FastAPI
from app.composer.composer_router import router as composer_router

app = FastAPI()

app.include_router(composer_router)

@app.get("/")
def root():
  return {"message": "Project Orchestra backend is live"}
