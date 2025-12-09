"""Hierarchical configuration for the AI backend."""

from typing import Any

from pydantic import ConfigDict, Field
from pydantic_settings import BaseSettings


class BaseConfig(BaseSettings):
    """Core settings (AWS region, credentials)."""

    model_config = ConfigDict(env_file=".env", env_file_encoding="utf-8")
    openai_api_key: str = Field(default="", json_schema_extra={"env": "OPENAI_API_KEY"})


class ModelConfig(BaseConfig):
    """Per-model configurations."""

    model: str = Field(default="gpt-5.1", json_schema_extra={"env": "MODEL"})
    max_completion_tokens: int = Field(default=5000, json_schema_extra={"env": "MAX_COMPLETION_TOKENS"})
    temperature: float = Field(default=0, json_schema_extra={"env": "TEMPERATURE"})


class EnvironmentConfig(ModelConfig):
    """Development/production overrides."""
    data_dir: str = Field(default="data", json_schema_extra={"env": "DATA_DIR"})  # noqa: E501
    log_level: str = Field(default="DEBUG", json_schema_extra={"env": "LOG_LEVEL"})


def get_settings() -> EnvironmentConfig:
    """Get application settings."""
    return EnvironmentConfig()
