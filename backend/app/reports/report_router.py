from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os

from .report_generator import generate_bounty_report

router = APIRouter()

REPORTS_DIR = "generated_reports"
os.makedirs(REPORTS_DIR, exist_ok=True)

class ReportRequest(BaseModel):
    title: str
    severity: str
    summary: str
    steps_to_reproduce: str
    impact: str
    recommendation: str

@router.post("/reports/create")
def create_report(request: ReportRequest):
    report_content = generate_bounty_report(
        request.title,
        request.severity,
        request.summary,
        request.steps_to_reproduce,
        request.impact,
        request.recommendation
    )

    safe_title = request.title.replace(" ", "_").replace("/", "_")
    file_path = os.path.join(REPORTS_DIR, f"{safe_title}.md")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(report_content)

    return {"message": "bountry report created successfully", "file_path": file_path}
