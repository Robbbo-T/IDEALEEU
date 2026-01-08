"""Tests for configuration module."""

import pytest
from config.settings import Settings, Environment, LogLevel, get_settings


class TestSettings:
    """Test cases for Settings class."""

    def test_settings_with_all_required_env_vars(self, monkeypatch):
        """Test settings initialization with all required environment variables."""
        # Set up environment variables
        monkeypatch.setenv("IDEALEEU_ENV", "dev")
        monkeypatch.setenv("IDEALEEU_LOG_LEVEL", "info")
        monkeypatch.setenv("IDEALEEU_DB_URL", "postgresql://user:pass@db:5432/ideale")
        monkeypatch.setenv("IDEALEEU_OBJECT_STORE", "s3://bucket/prefix")
        monkeypatch.setenv("OIDC_ISSUER_URL", "https://auth.example.com/")
        monkeypatch.setenv("OIDC_AUDIENCE", "ideale-api")
        monkeypatch.setenv("JWT_SIGNING_KEY", "test-secret-key")
        monkeypatch.setenv("EVENT_BUS_URL", "nats://nats:4222")

        # Clear the cache to ensure fresh settings
        get_settings.cache_clear()

        # Initialize settings
        settings = Settings()

        # Verify settings
        assert settings.env == Environment.DEV
        assert settings.log_level == LogLevel.INFO
        assert settings.db_url == "postgresql://user:pass@db:5432/ideale"
        assert settings.object_store == "s3://bucket/prefix"
        assert settings.oidc_issuer_url == "https://auth.example.com/"
        assert settings.oidc_audience == "ideale-api"
        assert settings.jwt_signing_key == "test-secret-key"
        assert settings.event_bus_url == "nats://nats:4222"

    def test_settings_missing_required_var(self, monkeypatch):
        """Test that missing required environment variable raises error."""
        # Clear all IDEALEEU environment variables first
        for key in [
            "IDEALEEU_ENV",
            "IDEALEEU_LOG_LEVEL",
            "IDEALEEU_DB_URL",
            "IDEALEEU_OBJECT_STORE",
            "OIDC_ISSUER_URL",
            "OIDC_AUDIENCE",
            "JWT_SIGNING_KEY",
            "EVENT_BUS_URL",
        ]:
            monkeypatch.delenv(key, raising=False)

        # Set only some environment variables
        monkeypatch.setenv("IDEALEEU_ENV", "dev")
        monkeypatch.setenv("IDEALEEU_LOG_LEVEL", "info")
        # Missing IDEALEEU_DB_URL

        # Clear the cache
        get_settings.cache_clear()

        # Verify error is raised
        with pytest.raises(ValueError, match="Required environment variable.*is not set"):
            Settings()

    def test_invalid_environment(self, monkeypatch):
        """Test that invalid environment value raises error."""
        monkeypatch.setenv("IDEALEEU_ENV", "invalid")
        monkeypatch.setenv("IDEALEEU_LOG_LEVEL", "info")
        monkeypatch.setenv("IDEALEEU_DB_URL", "postgresql://user:pass@db:5432/ideale")
        monkeypatch.setenv("IDEALEEU_OBJECT_STORE", "s3://bucket/prefix")
        monkeypatch.setenv("OIDC_ISSUER_URL", "https://auth.example.com/")
        monkeypatch.setenv("OIDC_AUDIENCE", "ideale-api")
        monkeypatch.setenv("JWT_SIGNING_KEY", "test-secret-key")
        monkeypatch.setenv("EVENT_BUS_URL", "nats://nats:4222")

        get_settings.cache_clear()

        with pytest.raises(ValueError, match="Invalid value.*Valid values"):
            Settings()

    def test_invalid_log_level(self, monkeypatch):
        """Test that invalid log level raises error."""
        monkeypatch.setenv("IDEALEEU_ENV", "dev")
        monkeypatch.setenv("IDEALEEU_LOG_LEVEL", "invalid")
        monkeypatch.setenv("IDEALEEU_DB_URL", "postgresql://user:pass@db:5432/ideale")
        monkeypatch.setenv("IDEALEEU_OBJECT_STORE", "s3://bucket/prefix")
        monkeypatch.setenv("OIDC_ISSUER_URL", "https://auth.example.com/")
        monkeypatch.setenv("OIDC_AUDIENCE", "ideale-api")
        monkeypatch.setenv("JWT_SIGNING_KEY", "test-secret-key")
        monkeypatch.setenv("EVENT_BUS_URL", "nats://nats:4222")

        get_settings.cache_clear()

        with pytest.raises(ValueError, match="Invalid value.*Valid values"):
            Settings()

    def test_invalid_db_url_format(self, monkeypatch):
        """Test that invalid database URL format raises error."""
        monkeypatch.setenv("IDEALEEU_ENV", "dev")
        monkeypatch.setenv("IDEALEEU_LOG_LEVEL", "info")
        monkeypatch.setenv("IDEALEEU_DB_URL", "mysql://user:pass@db:3306/ideale")
        monkeypatch.setenv("IDEALEEU_OBJECT_STORE", "s3://bucket/prefix")
        monkeypatch.setenv("OIDC_ISSUER_URL", "https://auth.example.com/")
        monkeypatch.setenv("OIDC_AUDIENCE", "ideale-api")
        monkeypatch.setenv("JWT_SIGNING_KEY", "test-secret-key")
        monkeypatch.setenv("EVENT_BUS_URL", "nats://nats:4222")

        get_settings.cache_clear()

        with pytest.raises(ValueError, match="must be a PostgreSQL connection string"):
            Settings()

    def test_invalid_object_store_format(self, monkeypatch):
        """Test that invalid object store URL format raises error."""
        monkeypatch.setenv("IDEALEEU_ENV", "dev")
        monkeypatch.setenv("IDEALEEU_LOG_LEVEL", "info")
        monkeypatch.setenv("IDEALEEU_DB_URL", "postgresql://user:pass@db:5432/ideale")
        monkeypatch.setenv("IDEALEEU_OBJECT_STORE", "http://bucket/prefix")
        monkeypatch.setenv("OIDC_ISSUER_URL", "https://auth.example.com/")
        monkeypatch.setenv("OIDC_AUDIENCE", "ideale-api")
        monkeypatch.setenv("JWT_SIGNING_KEY", "test-secret-key")
        monkeypatch.setenv("EVENT_BUS_URL", "nats://nats:4222")

        get_settings.cache_clear()

        with pytest.raises(ValueError, match="must be an S3-compatible URL"):
            Settings()

    def test_invalid_oidc_issuer_format(self, monkeypatch):
        """Test that invalid OIDC issuer URL format raises error."""
        monkeypatch.setenv("IDEALEEU_ENV", "dev")
        monkeypatch.setenv("IDEALEEU_LOG_LEVEL", "info")
        monkeypatch.setenv("IDEALEEU_DB_URL", "postgresql://user:pass@db:5432/ideale")
        monkeypatch.setenv("IDEALEEU_OBJECT_STORE", "s3://bucket/prefix")
        monkeypatch.setenv("OIDC_ISSUER_URL", "invalid-url")
        monkeypatch.setenv("OIDC_AUDIENCE", "ideale-api")
        monkeypatch.setenv("JWT_SIGNING_KEY", "test-secret-key")
        monkeypatch.setenv("EVENT_BUS_URL", "nats://nats:4222")

        get_settings.cache_clear()

        with pytest.raises(ValueError, match="must be a valid HTTP"):
            Settings()

    def test_invalid_event_bus_format(self, monkeypatch):
        """Test that invalid event bus URL format raises error."""
        monkeypatch.setenv("IDEALEEU_ENV", "dev")
        monkeypatch.setenv("IDEALEEU_LOG_LEVEL", "info")
        monkeypatch.setenv("IDEALEEU_DB_URL", "postgresql://user:pass@db:5432/ideale")
        monkeypatch.setenv("IDEALEEU_OBJECT_STORE", "s3://bucket/prefix")
        monkeypatch.setenv("OIDC_ISSUER_URL", "https://auth.example.com/")
        monkeypatch.setenv("OIDC_AUDIENCE", "ideale-api")
        monkeypatch.setenv("JWT_SIGNING_KEY", "test-secret-key")
        monkeypatch.setenv("EVENT_BUS_URL", "http://nats:4222")

        get_settings.cache_clear()

        with pytest.raises(ValueError, match="must be a NATS connection string"):
            Settings()

    def test_production_with_default_jwt_key(self, monkeypatch):
        """Test that production environment with default JWT key raises error."""
        monkeypatch.setenv("IDEALEEU_ENV", "production")
        monkeypatch.setenv("IDEALEEU_LOG_LEVEL", "info")
        monkeypatch.setenv("IDEALEEU_DB_URL", "postgresql://user:pass@db:5432/ideale")
        monkeypatch.setenv("IDEALEEU_OBJECT_STORE", "s3://bucket/prefix")
        monkeypatch.setenv("OIDC_ISSUER_URL", "https://auth.example.com/")
        monkeypatch.setenv("OIDC_AUDIENCE", "ideale-api")
        monkeypatch.setenv("JWT_SIGNING_KEY", "change-me")
        monkeypatch.setenv("EVENT_BUS_URL", "nats://nats:4222")

        get_settings.cache_clear()

        with pytest.raises(ValueError, match="must be changed from default value"):
            Settings()

    def test_environment_properties(self, monkeypatch):
        """Test environment property helpers."""
        monkeypatch.setenv("IDEALEEU_ENV", "dev")
        monkeypatch.setenv("IDEALEEU_LOG_LEVEL", "info")
        monkeypatch.setenv("IDEALEEU_DB_URL", "postgresql://user:pass@db:5432/ideale")
        monkeypatch.setenv("IDEALEEU_OBJECT_STORE", "s3://bucket/prefix")
        monkeypatch.setenv("OIDC_ISSUER_URL", "https://auth.example.com/")
        monkeypatch.setenv("OIDC_AUDIENCE", "ideale-api")
        monkeypatch.setenv("JWT_SIGNING_KEY", "test-secret-key")
        monkeypatch.setenv("EVENT_BUS_URL", "nats://nats:4222")

        get_settings.cache_clear()
        settings = Settings()

        assert settings.is_dev is True
        assert settings.is_staging is False
        assert settings.is_production is False

    def test_get_settings_caching(self, monkeypatch):
        """Test that get_settings returns cached instance."""
        monkeypatch.setenv("IDEALEEU_ENV", "dev")
        monkeypatch.setenv("IDEALEEU_LOG_LEVEL", "info")
        monkeypatch.setenv("IDEALEEU_DB_URL", "postgresql://user:pass@db:5432/ideale")
        monkeypatch.setenv("IDEALEEU_OBJECT_STORE", "s3://bucket/prefix")
        monkeypatch.setenv("OIDC_ISSUER_URL", "https://auth.example.com/")
        monkeypatch.setenv("OIDC_AUDIENCE", "ideale-api")
        monkeypatch.setenv("JWT_SIGNING_KEY", "test-secret-key")
        monkeypatch.setenv("EVENT_BUS_URL", "nats://nats:4222")

        get_settings.cache_clear()

        settings1 = get_settings()
        settings2 = get_settings()

        assert settings1 is settings2

    def test_settings_repr_no_sensitive_data(self, monkeypatch):
        """Test that __repr__ doesn't expose sensitive data."""
        monkeypatch.setenv("IDEALEEU_ENV", "dev")
        monkeypatch.setenv("IDEALEEU_LOG_LEVEL", "info")
        monkeypatch.setenv("IDEALEEU_DB_URL", "postgresql://user:pass@db:5432/ideale")
        monkeypatch.setenv("IDEALEEU_OBJECT_STORE", "s3://bucket/prefix")
        monkeypatch.setenv("OIDC_ISSUER_URL", "https://auth.example.com/")
        monkeypatch.setenv("OIDC_AUDIENCE", "ideale-api")
        monkeypatch.setenv("JWT_SIGNING_KEY", "test-secret-key")
        monkeypatch.setenv("EVENT_BUS_URL", "nats://nats:4222")

        get_settings.cache_clear()
        settings = Settings()

        repr_str = repr(settings)

        # Should not contain passwords or full connection strings
        assert "pass" not in repr_str.lower() or "***" in repr_str
        assert "test-secret-key" not in repr_str
