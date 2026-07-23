from app.application.analyze_code import AnalyzeCodeUseCase
from app.infrastructure.static_code_analyzer import StaticCodeAnalyzer


def get_analyze_code_use_case() -> AnalyzeCodeUseCase:
    return AnalyzeCodeUseCase(analyzer=StaticCodeAnalyzer())
