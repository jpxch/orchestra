from fastapi import FastAPI
from app.composer.composer_router import router as composer_router
from app.reports.report_router import router as report_router

app = FastAPI()

app.include_router(composer_router)
app.include_router(report_router)

@app.get("/")
def root():
  return {"message": "Project Orchestra backend is live"}
