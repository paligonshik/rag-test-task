"""Error classification for the AI backend template."""

from enum import StrEnum, auto
from typing import Any


class AIBackendError(Exception):
    """Base exception for AI backend errors."""

    def __init__(self, message: str, details: dict[str, Any] | None = None) -> None:
        """Initialize the AIBackendError."""
        super().__init__(message)
        self.message = message
        self.details = details or {}


class TransientError(AIBackendError):
    """Retry-able errors (rate limits, timeouts)."""

    def __init__(
        self,
        message: str,
        retry_after: int | None = None,
        details: dict[str, Any] | None = None,
    ) -> None:
        """Initialize the TransientError."""
        super().__init__(message, details)
        self.retry_after = retry_after


class PermanentError(AIBackendError):
    """Non-retry-able errors (invalid input)."""


class ModelError(AIBackendError):
    """Model-specific errors with custom handling."""

    def __init__(
        self,
        message: str,
        model_id: str,
        error_code: str | None = None,
        details: dict[str, Any] | None = None,
    ) -> None:
        """Initialize the ModelError."""
        super().__init__(message, details)
        self.model_id = model_id
        self.error_code = error_code


class ConfigurationError(PermanentError):
    """Configuration-related errors."""


class AuthenticationError(PermanentError):
    """Authentication and authorization errors."""


class RateLimitError(TransientError):
    """Rate limiting errors."""

    def __init__(
        self,
        message: str,
        retry_after: int | None = None,
        limit_type: str | None = None,
        details: dict[str, Any] | None = None,
    ) -> None:
        """Initialize the RateLimitError."""
        super().__init__(message, retry_after, details)
        self.limit_type = limit_type


class RequestTimeoutError(TransientError):
    """Request timeout errors."""


class ValidationError(PermanentError):
    """Input validation errors."""


class LLMOutputError(PermanentError):
    """LLM output errors."""

    def __init__(
        self,
        message: str,
        details: dict[str, Any] | None = None,
    ) -> None:
        """Initialize the LLMOutputError."""
        super().__init__(message, details)


class DataLoadError(PermanentError):
    """Data loading errors (file not found, corrupted data)."""


class QueryExecutionError(PermanentError):
    """Query execution errors (invalid parameters, Pandas errors)."""


class SchemaError(PermanentError):
    """Schema-related errors (column not found, type mismatch)."""
