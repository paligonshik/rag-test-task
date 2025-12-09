"""Shared type definitions used across the AI backend packages."""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field
from enum import StrEnum, auto
from typing import Any


class MessageRole(StrEnum):
    """Allowed roles for chat messages."""

    SYSTEM = auto()
    USER = auto()
    ASSISTANT = auto()


@dataclass
class Message:
    """Represents a single chat message exchanged with an agent or model."""

    role: MessageRole
    content: str


@dataclass
class AgentConfig:
    """Configuration values that are common to all agents."""

    agent_type: str
    model_id: str
    extra: dict[str, Any] = field(default_factory=dict)


@dataclass
class AgentRequest:
    """A generic request object passed to an agent's ``process`` method."""

    question: str
    context: Sequence[Message] | None = None


@dataclass
class AgentResponse:
    """A generic response returned from an agent's `process` method."""

    answer: str
    citations: list[Any] | None = None
    raw: Any | None = None


@dataclass
class LLMResponse:
    """A class representing a LLM response."""

    content: Any
