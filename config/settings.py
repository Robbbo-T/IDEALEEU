"""IDEALEEU Settings Module.

Centralized configuration management using environment variables.
All settings are loaded from environment variables with validation.
"""

import os
from enum import Enum
from functools import lru_cache


class Environment(str, Enum):
    """Valid environment types."""

    DEV = "dev"
    STAGING = "staging"
    PRODUCTION = "production"


class LogLevel(str, Enum):
    """Valid logging levels."""

    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


class Settings:
    """IDEALEEU platform configuration settings.

    All settings are loaded from environment variables with the IDEALEEU_ prefix
    (except for OIDC, JWT, and EVENT_BUS which use their standard prefixes).

    Required environment variables:
    - IDEALEEU_ENV: Environment (dev, staging, production)
    - IDEALEEU_LOG_LEVEL: Logging level (debug, info, warning, error, critical)
    - IDEALEEU_DB_URL: Database connection URL
    - IDEALEEU_OBJECT_STORE: Object storage URL (S3-compatible)
    - OIDC_ISSUER_URL: OpenID Connect issuer URL
    - OIDC_AUDIENCE: OIDC audience identifier
    - JWT_SIGNING_KEY: JWT signing key (must be changed in production)
    - EVENT_BUS_URL: Event bus connection URL (NATS)
    """

    def __init__(self) -> None:
        """Initialize settings from environment variables."""
        # Core application settings
        self.env: Environment = self._get_env("IDEALEEU_ENV", Environment.DEV)
        self.log_level: LogLevel = self._get_log_level("IDEALEEU_LOG_LEVEL", LogLevel.INFO)

        # Database configuration
        self.db_url: str = self._get_required("IDEALEEU_DB_URL")

        # Object storage configuration
        self.object_store: str = self._get_required("IDEALEEU_OBJECT_STORE")

        # Authentication configuration
        self.oidc_issuer_url: str = self._get_required("OIDC_ISSUER_URL")
        self.oidc_audience: str = self._get_required("OIDC_AUDIENCE")
        self.jwt_signing_key: str = self._get_required("JWT_SIGNING_KEY")

        # Event bus configuration
        self.event_bus_url: str = self._get_required("EVENT_BUS_URL")

        # Validate configuration
        self._validate()

    def _get_required(self, key: str) -> str:
        """Get a required environment variable.

        Args:
            key: Environment variable name

        Returns:
            Environment variable value

        Raises:
            ValueError: If environment variable is not set
        """
        value = os.getenv(key)
        if not value:
            raise ValueError(f"Required environment variable {key} is not set")
        return value

    def _get_env(self, key: str, default: Environment) -> Environment:
        """Get environment type from environment variable.

        Args:
            key: Environment variable name
            default: Default environment if not set

        Returns:
            Environment enum value
        """
        value = os.getenv(key, default.value).lower()
        try:
            return Environment(value)
        except ValueError:
            valid_values = ", ".join([e.value for e in Environment])
            raise ValueError(f"Invalid value '{value}' for {key}. " f"Valid values: {valid_values}")

    def _get_log_level(self, key: str, default: LogLevel) -> LogLevel:
        """Get log level from environment variable.

        Args:
            key: Environment variable name
            default: Default log level if not set

        Returns:
            LogLevel enum value
        """
        value = os.getenv(key, default.value).lower()
        try:
            return LogLevel(value)
        except ValueError:
            valid_values = ", ".join([e.value for e in LogLevel])
            raise ValueError(f"Invalid value '{value}' for {key}. " f"Valid values: {valid_values}")

    def _validate(self) -> None:
        """Validate configuration settings.

        Raises:
            ValueError: If configuration is invalid
        """
        # Validate database URL format
        if not self.db_url.startswith(("postgresql://", "postgres://")):
            raise ValueError(
                "IDEALEEU_DB_URL must be a PostgreSQL connection string "
                "(postgresql:// or postgres://)"
            )

        # Validate object store URL format
        if not self.object_store.startswith("s3://"):
            raise ValueError("IDEALEEU_OBJECT_STORE must be an S3-compatible URL (s3://)")

        # Validate OIDC issuer URL format
        if not self.oidc_issuer_url.startswith(("https://", "http://")):
            raise ValueError("OIDC_ISSUER_URL must be a valid HTTP(S) URL")

        # Validate event bus URL format
        if not self.event_bus_url.startswith("nats://"):
            raise ValueError("EVENT_BUS_URL must be a NATS connection string (nats://)")

        # Warn about insecure JWT signing key in production
        if self.env == Environment.PRODUCTION and self.jwt_signing_key == "change-me":
            raise ValueError("JWT_SIGNING_KEY must be changed from default value in production")

    @property
    def is_dev(self) -> bool:
        """Check if running in development environment."""
        return self.env == Environment.DEV

    @property
    def is_staging(self) -> bool:
        """Check if running in staging environment."""
        return self.env == Environment.STAGING

    @property
    def is_production(self) -> bool:
        """Check if running in production environment."""
        return self.env == Environment.PRODUCTION

    def __repr__(self) -> str:
        """Return string representation of settings (without sensitive data)."""
        event_bus_display = (
            self.event_bus_url.split("@")[0]
            if "@" in self.event_bus_url
            else self.event_bus_url
        )
        return (
            f"Settings(env={self.env.value}, log_level={self.log_level.value}, "
            f"db_url={'***' if self.db_url else 'not set'}, "
            f"object_store={self.object_store.split('/')[0]}//, "
            f"oidc_issuer_url={self.oidc_issuer_url}, "
            f"event_bus_url={event_bus_display})"
        )


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance.

    This function uses lru_cache to ensure only one Settings instance
    is created and reused across the application.

    Returns:
        Settings instance
    """
    return Settings()
