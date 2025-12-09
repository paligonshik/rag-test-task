"""Structured logging with correlation IDs for the AI backend."""

import uuid
from contextvars import ContextVar
from typing import Any

import structlog

# Context variable for correlation ID
correlation_id_ctx: ContextVar[str] = ContextVar("correlation_id", default="")


def configure_logging() -> None:
    """Configure structured logging."""
    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            add_correlation_id,
            structlog.dev.ConsoleRenderer()
            if __debug__
            else structlog.processors.JSONRenderer(),
        ],
        wrapper_class=structlog.make_filtering_bound_logger(20),  # INFO level
        logger_factory=structlog.WriteLoggerFactory(),
        cache_logger_on_first_use=True,
    )


def add_correlation_id(
    logger: structlog.BoundLogger,  # noqa: ARG001
    method_name: str,  # noqa: ARG001
    event_dict: dict[str, Any],
) -> dict[str, Any]:
    """Add correlation ID to log entries."""
    correlation_id = correlation_id_ctx.get()
    if correlation_id:
        event_dict["correlation_id"] = correlation_id
    return event_dict


def set_correlation_id(correlation_id: str | None = None) -> str:
    """Set correlation ID for the current context."""
    if correlation_id is None:
        correlation_id = str(uuid.uuid4())
    correlation_id_ctx.set(correlation_id)
    return correlation_id


def get_correlation_id() -> str:
    """Get current correlation ID."""
    return correlation_id_ctx.get()


class StructuredLogger:
    """Structured logger with correlation ID support."""

    def __init__(self, name: str) -> None:
        """Initialize the StructuredLogger."""
        self.logger = structlog.get_logger(name)

    def debug(self, message: str, **kwargs: Any) -> None:  # noqa: ANN401
        """Log debug message."""
        self.logger.debug(message, **kwargs)

    def info(self, message: str, **kwargs: Any) -> None:  # noqa: ANN401
        """Log info message."""
        self.logger.info(message, **kwargs)

    def warning(self, message: str, **kwargs: Any) -> None:  # noqa: ANN401
        """Log warning message."""
        self.logger.warning(message, **kwargs)

    def error(self, message: str, **kwargs: Any) -> None:  # noqa: ANN401
        """Log error message."""
        self.logger.error(message, **kwargs)

    def exception(self, message: str, **kwargs: Any) -> None:  # noqa: ANN401
        """Log exception with traceback."""
        self.logger.exception(message, **kwargs)

    def critical(self, message: str, **kwargs: Any) -> None:  # noqa: ANN401
        """Log critical message."""
        self.logger.critical(message, **kwargs)


# Initialize logging configuration
configure_logging()
