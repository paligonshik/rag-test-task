"""OpenAI client wrapper for code generation and response formatting."""

import re
from dataclasses import dataclass

from openai import OpenAI

from src.config.settings import get_settings
from src.llm.prompt import (
    CODE_GENERATION_SYSTEM_PROMPT,
    RESPONSE_FORMATTING_SYSTEM_PROMPT,
    get_code_generation_prompt,
    get_response_formatting_prompt,
)


@dataclass
class LLMResponse:
    """Response from LLM operations."""

    content: str
    model: str
    usage: dict[str, int]


class OpenAIClient:
    """Client for interacting with OpenAI API."""

    def __init__(
        self,
        api_key: str | None = None,
        model: str | None = None,
    ) -> None:
        """Initialize the OpenAI client.

        Args:
            api_key: OpenAI API key. If None, uses OPENAI_API_KEY env var.
            model: Model to use for completions. If None, uses settings default.
        """
        settings = get_settings()
        self.client = OpenAI(api_key=api_key)
        self.model = model or settings.model
        self._settings = settings

    def generate_query_code(self, question: str) -> LLMResponse:
        """Generate pandas code to answer a question.

        Args:
            question: Natural language question about the data.

        Returns:
            LLMResponse containing the generated code.
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": CODE_GENERATION_SYSTEM_PROMPT},
                {"role": "user", "content": get_code_generation_prompt(question)},
            ],
            temperature=self._settings.temperature,
            max_completion_tokens=self._settings.max_completion_tokens,
        )

        content = response.choices[0].message.content or ""
        # Extract code from markdown code blocks if present
        content = self._extract_code(content)

        return LLMResponse(
            content=content,
            model=response.model,
            usage={
                "prompt_tokens": response.usage.prompt_tokens if response.usage else 0,
                "completion_tokens": (
                    response.usage.completion_tokens if response.usage else 0
                ),
                "total_tokens": response.usage.total_tokens if response.usage else 0,
            },
        )

    def format_response(self, question: str, data_result: str) -> LLMResponse:
        """Format query results into a natural language response.

        Args:
            question: Original user question.
            data_result: String representation of query results.

        Returns:
            LLMResponse containing the formatted answer.
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": RESPONSE_FORMATTING_SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": get_response_formatting_prompt(question, data_result),
                },
            ],
            temperature=self._settings.temperature,
            max_completion_tokens=self._settings.max_completion_tokens,
        )

        return LLMResponse(
            content=response.choices[0].message.content or "",
            model=response.model,
            usage={
                "prompt_tokens": response.usage.prompt_tokens if response.usage else 0,
                "completion_tokens": (
                    response.usage.completion_tokens if response.usage else 0
                ),
                "total_tokens": response.usage.total_tokens if response.usage else 0,
            },
        )

    def _extract_code(self, content: str) -> str:
        """Extract Python code from markdown code blocks.

        Args:
            content: Raw LLM output that may contain markdown.

        Returns:
            Clean Python code.
        """
        # Try to extract from ```python ... ``` blocks
        pattern = r"```(?:python)?\s*\n?(.*?)```"
        matches = re.findall(pattern, content, re.DOTALL)
        if matches:
            return matches[0].strip()
        # If no code blocks, return as-is (might already be clean code)
        return content.strip()

