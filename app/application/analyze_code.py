from app.domain.models import AnalysisResult, CodeInput
from app.domain.ports import CodeAnalyzer


class AnalyzeCodeUseCase:
    def __init__(self, analyzer: CodeAnalyzer) -> None:
        self._analyzer = analyzer

    def execute(self, code_input: CodeInput) -> AnalysisResult:
        return self._analyzer.analyze(code_input)
