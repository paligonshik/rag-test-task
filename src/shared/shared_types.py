"""Shared type definitions used across the AI backend packages."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum, auto


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
