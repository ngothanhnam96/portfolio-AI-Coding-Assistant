import ast
import re
from textwrap import dedent

from app.domain.models import AnalysisResult, AnalysisTask, CodeInput


class StaticCodeAnalyzer:
    """Small deterministic analyzer for portfolio demos and tests."""

    def analyze(self, code_input: CodeInput) -> AnalysisResult:
        normalized_code = dedent(code_input.code).strip()
        task_handlers = {
            AnalysisTask.EXPLAIN_CODE: self._explain_code,
            AnalysisTask.REFACTOR: self._refactor,
            AnalysisTask.BUG_DETECTION: self._detect_bugs,
            AnalysisTask.UNIT_TEST: self._unit_tests,
            AnalysisTask.UML: self._uml,
            AnalysisTask.CODE_SUMMARY: self._summary,
        }
        return task_handlers[code_input.task](code_input, normalized_code)

    def _explain_code(self, code_input: CodeInput, code: str) -> AnalysisResult:
        functions, classes = self._python_symbols(code)
        parts = [
            f"This {code_input.language} snippet contains {len(code.splitlines())} line(s).",
            self._symbol_sentence(functions, classes),
            "It should be reviewed for inputs, return values, side effects, and error handling.",
        ]
        return self._result(code_input, " ".join(parts))

    def _refactor(self, code_input: CodeInput, code: str) -> AnalysisResult:
        suggestions = [
            "Extract complex logic into small named functions.",
            "Use clear parameter names and avoid hidden side effects.",
            "Add type hints or interface contracts where supported.",
        ]
        if len(code.splitlines()) > 40:
            suggestions.append("Split the file into smaller modules with one responsibility each.")
        if re.search(r"\b(if|for|while)\b", code) and "return" not in code:
            suggestions.append("Return explicit values from branches that compute data.")
        return self._result(
            code_input,
            "Refactor suggestions focus on readability, testability, and single responsibility.",
            suggestions=suggestions,
        )

    def _detect_bugs(self, code_input: CodeInput, code: str) -> AnalysisResult:
        findings: list[str] = []
        if re.search(r"/\s*[a-zA-Z_][a-zA-Z0-9_]*", code):
            findings.append("Possible division by zero if the denominator is not validated.")
        if "except:" in code:
            findings.append("Bare except can hide real failures and make debugging harder.")
        if re.search(r"\b(eval|exec)\s*\(", code):
            findings.append("Dynamic execution can introduce security vulnerabilities.")
        if "TODO" in code or "FIXME" in code:
            findings.append("Unresolved TODO/FIXME comments may indicate incomplete behavior.")
        if not findings:
            findings.append("No obvious high-risk pattern was detected by the static analyzer.")
        return self._result(code_input, "Bug detection completed.", findings=findings)

    def _unit_tests(self, code_input: CodeInput, code: str) -> AnalysisResult:
        functions, _ = self._python_symbols(code)
        target = ", ".join(functions) if functions else "the main behavior"
        suggestions = [
            f"Test the happy path for {target}.",
            "Test invalid, empty, or boundary inputs.",
            "Test error handling and expected exceptions.",
        ]
        return self._result(
            code_input,
            "Recommended unit-test scenarios generated.",
            suggestions=suggestions,
        )

    def _uml(self, code_input: CodeInput, code: str) -> AnalysisResult:
        functions, classes = self._python_symbols(code)
        if classes:
            lines = ["classDiagram"]
            lines.extend(f"    class {class_name}" for class_name in classes)
        else:
            lines = ["flowchart TD", "    A[Start] --> B[Read input]"]
            for index, function_name in enumerate(functions or ["process"], start=1):
                lines.append(f"    B --> F{index}[{function_name}()]")
            lines.append("    B --> C[Return result]")
        return self._result(code_input, "\n".join(lines))

    def _summary(self, code_input: CodeInput, code: str) -> AnalysisResult:
        functions, classes = self._python_symbols(code)
        result = (
            f"Summary: {len(code.splitlines())} line(s), "
            f"{len(functions)} function(s), {len(classes)} class(es). "
            f"{self._symbol_sentence(functions, classes)}"
        )
        return self._result(code_input, result)

    def _result(
        self,
        code_input: CodeInput,
        result: str,
        findings: list[str] | None = None,
        suggestions: list[str] | None = None,
    ) -> AnalysisResult:
        return AnalysisResult(
            task=code_input.task,
            language=code_input.language,
            result=result,
            findings=findings or [],
            suggestions=suggestions or [],
        )

    def _python_symbols(self, code: str) -> tuple[list[str], list[str]]:
        try:
            tree = ast.parse(code)
        except SyntaxError:
            return [], []

        functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
        return functions, classes

    def _symbol_sentence(self, functions: list[str], classes: list[str]) -> str:
        details: list[str] = []
        if classes:
            details.append(f"class(es): {', '.join(classes)}")
        if functions:
            details.append(f"function(s): {', '.join(functions)}")
        if not details:
            return "No Python symbols were detected."
        return "Detected " + "; ".join(details) + "."

