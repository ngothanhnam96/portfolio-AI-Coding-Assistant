from typing import Protocol

from app.domain.models import AnalysisResult, CodeInput


class CodeAnalyzer(Protocol):
    def analyze(self, code_input: CodeInput) -> AnalysisResult:
        """Analyze a code snippet for a requested task."""
