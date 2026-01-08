# IDEALEEU Configuration Module

This module provides centralized configuration management for the IDEALEEU platform using environment variables.

## Overview

The configuration module loads and validates all required environment variables at startup, ensuring that the application has a valid configuration before proceeding.

## Features

- **Type-safe configuration**: Uses Python enums for environments and log levels
- **Validation**: Validates all configuration values at startup
- **Caching**: Settings are cached for performance using `@lru_cache`
- **Security**: Prevents sensitive data from being exposed in logs or error messages
- **Environment-aware**: Provides helper properties to check the current environment

## Required Environment Variables

All configuration is loaded from environment variables:

### Core Application Settings

- `IDEALEEU_ENV`: Environment type (dev, staging, production)
- `IDEALEEU_LOG_LEVEL`: Logging level (debug, info, warning, error, critical)

### Database Configuration

- `IDEALEEU_DB_URL`: PostgreSQL connection string (e.g., `postgresql://user:pass@db:5432/ideale`)

### Object Storage Configuration

- `IDEALEEU_OBJECT_STORE`: S3-compatible object storage URL (e.g., `s3://bucket/prefix`)

### Authentication Configuration

- `OIDC_ISSUER_URL`: OpenID Connect issuer URL (e.g., `https://auth.example.com/`)
- `OIDC_AUDIENCE`: OIDC audience identifier (e.g., `ideale-api`)
- `JWT_SIGNING_KEY`: JWT signing key (must be changed from default in production)

### Event Bus Configuration

- `EVENT_BUS_URL`: NATS event bus connection URL (e.g., `nats://nats:4222`)

## Usage

### Basic Usage

```python
from config import get_settings

# Load settings (cached for subsequent calls)
settings = get_settings()

# Access configuration values
print(f"Environment: {settings.env.value}")
print(f"Database: {settings.db_url}")
print(f"Log Level: {settings.log_level.value}")
```

### Environment Checks

```python
from config import get_settings

settings = get_settings()

if settings.is_production:
    # Production-specific logic
    pass
elif settings.is_dev:
    # Development-specific logic
    pass
```

### FastAPI Integration

```python
from fastapi import FastAPI, Depends
from config import Settings, get_settings

app = FastAPI()

@app.get("/health")
async def health_check(settings: Settings = Depends(get_settings)):
    return {
        "status": "healthy",
        "environment": settings.env.value
    }
```

## Setup

### Development Setup

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` with your local configuration values

3. Load environment variables (automatic in most frameworks):
   ```bash
   # If using python-dotenv
   export $(cat .env | xargs)
   ```

### Production Setup

**Important**: Never commit secrets to version control!

In production, use your orchestrator's secret management:

- **Kubernetes**: Use ConfigMaps and Secrets
- **Docker Compose**: Use environment files and secrets
- **Cloud platforms**: Use native secret management (AWS Secrets Manager, Azure Key Vault, etc.)

## Validation

The configuration module performs the following validations:

1. **Required variables**: All required environment variables must be set
2. **Environment type**: Must be one of: dev, staging, production
3. **Log level**: Must be one of: debug, info, warning, error, critical
4. **Database URL**: Must be a PostgreSQL connection string (postgresql:// or postgres://)
5. **Object store URL**: Must be an S3-compatible URL (s3://)
6. **OIDC issuer URL**: Must be a valid HTTP(S) URL
7. **Event bus URL**: Must be a NATS connection string (nats://)
8. **JWT signing key**: Must not be the default value in production

## Testing

Run the configuration tests:

```bash
pytest config/tests/test_settings.py -v
```

Run the example usage script:

```bash
export IDEALEEU_ENV=dev
export IDEALEEU_LOG_LEVEL=info
export IDEALEEU_DB_URL=postgresql://user:pass@db:5432/ideale
export IDEALEEU_OBJECT_STORE=s3://bucket/prefix
export OIDC_ISSUER_URL=https://auth.example.com/
export OIDC_AUDIENCE=ideale-api
export JWT_SIGNING_KEY=change-me
export EVENT_BUS_URL=nats://nats:4222

PYTHONPATH=. python3 config/example_usage.py
```

## Security Best Practices

1. **Never commit `.env` files** with real secrets to version control
2. **Use strong, unique values** for JWT_SIGNING_KEY in production
3. **Rotate secrets regularly** using your secret management system
4. **Use HTTPS** for all external service URLs in production
5. **Restrict database access** using firewall rules and authentication
6. **Enable audit logging** for all configuration changes

## Error Handling

The configuration module will raise `ValueError` with descriptive messages if:

- Required environment variables are missing
- Configuration values have invalid formats
- Production environment uses insecure defaults

Example error messages:

```
ValueError: Required environment variable IDEALEEU_DB_URL is not set
ValueError: IDEALEEU_DB_URL must be a PostgreSQL connection string (postgresql:// or postgres://)
ValueError: JWT_SIGNING_KEY must be changed from default value in production
```

## Architecture

The configuration module uses a singleton pattern via `@lru_cache` to ensure that:

1. Settings are loaded only once per application instance
2. Validation occurs at startup, failing fast if misconfigured
3. Performance is optimized by caching the settings object

## Contributing

When adding new configuration options:

1. Add the environment variable to `.env.example` with a description
2. Add validation logic to `Settings._validate()`
3. Add comprehensive tests in `config/tests/test_settings.py`
4. Update this README with the new configuration option
5. Update the main README.md if the option is critical

## License

This module is part of the IDEALEEU platform and follows the repository's license.
