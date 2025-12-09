"""Safe code executor for pandas queries."""

from dataclasses import dataclass
from typing import Any

import pandas as pd


@dataclass
class ExecutionResult:
    """Result of code execution."""

    success: bool
    result: Any
    error: str | None = None
    result_type: str = ""

    def to_string(self) -> str:
        """Convert result to string for LLM consumption."""
        if not self.success:
            return f"Error: {self.error}"

        if isinstance(self.result, pd.DataFrame):
            if len(self.result) == 0:
                return "No results found (empty DataFrame)"
            # Limit output for very large results
            if len(self.result) > 50:
                return (
                    f"DataFrame with {len(self.result)} rows. "
                    f"First 50 rows:\n{self.result.head(50).to_string()}"
                )
            return self.result.to_string()

        if isinstance(self.result, pd.Series):
            return self.result.to_string()

        if isinstance(self.result, dict):
            return str(self.result)

        return str(self.result)


class CodeExecutor:
    """Executes pandas code in a sandboxed environment."""

    # Allowed built-in functions for safety
    ALLOWED_BUILTINS = {
        "len": len,
        "sum": sum,
        "min": min,
        "max": max,
        "abs": abs,
        "round": round,
        "sorted": sorted,
        "list": list,
        "dict": dict,
        "str": str,
        "int": int,
        "float": float,
        "bool": bool,
        "tuple": tuple,
        "set": set,
        "range": range,
        "enumerate": enumerate,
        "zip": zip,
        "map": map,
        "filter": filter,
        "True": True,
        "False": False,
        "None": None,
    }

    def __init__(self, dataframes: dict[str, pd.DataFrame]) -> None:
        """Initialize executor with dataframes.

        Args:
            dataframes: Dict mapping names to DataFrames.
        """
        self.dataframes = dataframes

    def execute(self, code: str) -> ExecutionResult:
        """Execute pandas code safely.

        Args:
            code: Python code to execute.

        Returns:
            ExecutionResult with the outcome.
        """
        # Build execution context with limited scope
        exec_globals: dict[str, Any] = {
            "__builtins__": self.ALLOWED_BUILTINS,
            "pd": pd,
        }

        # Add dataframes to context
        exec_locals: dict[str, Any] = dict(self.dataframes)

        try:
            # Execute the code
            exec(code, exec_globals, exec_locals)  # noqa: S102

            # Get the result variable
            if "result" not in exec_locals:
                return ExecutionResult(
                    success=False,
                    result=None,
                    error="Code did not produce a 'result' variable",
                )

            result = exec_locals["result"]

            return ExecutionResult(
                success=True,
                result=result,
                result_type=type(result).__name__,
            )

        except Exception as e:
            return ExecutionResult(
                success=False,
                result=None,
                error=f"{type(e).__name__}: {e!s}",
            )

