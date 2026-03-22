"""Hierarchical configuration for the AI backend."""

from pydantic import ConfigDict, Field
from pydantic_settings import BaseSettings


class BaseConfig(BaseSettings):
    """Core settings loaded from environment variables or .env file."""

    model_config = ConfigDict(env_file=".env", env_file_encoding="utf-8")
    openai_api_key: str = Field(default="")


class ModelConfig(BaseConfig):
    """Per-model configurations."""

    model: str = Field(default="gpt-5.1")
    max_completion_tokens: int = Field(default=5000)
    temperature: float = Field(default=0)


class EnvironmentConfig(ModelConfig):
    """Development/production overrides."""

    data_dir: str = Field(default="data")
    log_level: str = Field(default="DEBUG")


def get_settings() -> EnvironmentConfig:
    """Get application settings."""
    return EnvironmentConfig()
