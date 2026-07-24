from fastapi import APIRouter, Depends

from app.api.dependencies import get_analyze_code_use_case
from app.application.analyze_code import AnalyzeCodeUseCase
from app.domain.models import AnalysisResult, CodeInput

router = APIRouter(tags=["analysis"])


@router.post("/analyze", response_model=AnalysisResult)
def analyze_code(
    payload: CodeInput,
    use_case: AnalyzeCodeUseCase = Depends(get_analyze_code_use_case),
) -> AnalysisResult:
    return use_case.execute(payload)
