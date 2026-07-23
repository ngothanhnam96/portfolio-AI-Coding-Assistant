from enum import Enum

from pydantic import BaseModel, Field


class AnalysisTask(str, Enum):
    EXPLAIN_CODE = "explain_code"
    REFACTOR = "refactor"
    BUG_DETECTION = "bug_detection"
    UNIT_TEST = "unit_test"
    UML = "uml"
    CODE_SUMMARY = "code_summary"


class CodeInput(BaseModel):
    task: AnalysisTask
    language: str = Field(min_length=1, max_length=40)
    code: str = Field(min_length=1)
    file_name: str | None = Field(default=None, max_length=120)


class AnalysisResult(BaseModel):
    task: AnalysisTask
    language: str
    result: str
    findings: list[str] = Field(default_factory=list)
    suggestions: list[str] = Field(default_factory=list)
