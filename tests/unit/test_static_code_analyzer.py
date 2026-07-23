from app.domain.models import AnalysisTask, CodeInput
from app.infrastructure.static_code_analyzer import StaticCodeAnalyzer


def test_bug_detection_flags_possible_division_by_zero() -> None:
    analyzer = StaticCodeAnalyzer()

    result = analyzer.analyze(
        CodeInput(
            task=AnalysisTask.BUG_DETECTION,
            language="python",
            code="def divide(a, b):\n    return a / b",
        )
    )

    assert result.findings
    assert "division by zero" in result.findings[0]


def test_summary_counts_python_symbols() -> None:
    analyzer = StaticCodeAnalyzer()

    result = analyzer.analyze(
        CodeInput(
            task=AnalysisTask.CODE_SUMMARY,
            language="python",
            code="class Calculator:\n    def add(self, a, b):\n        return a + b",
        )
    )

    assert "1 function(s)" in result.result
    assert "1 class(es)" in result.result
