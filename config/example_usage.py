"""Example usage of IDEALEEU configuration.

This script demonstrates how to use the configuration module
to load and access environment-based settings.
"""

import sys
from config import get_settings


def main():
    """Load and display configuration settings."""
    try:
        # Load settings (will raise error if required env vars are missing)
        settings = get_settings()

        print("=" * 60)
        print("IDEALEEU Configuration")
        print("=" * 60)
        print()

        print(f"Environment: {settings.env.value}")
        print(f"Log Level: {settings.log_level.value}")
        print()

        print("Database Configuration:")
        db_display = (
            settings.db_url.split("@")[0] + "@***"
            if "@" in settings.db_url
            else "***"
        )
        print(f"  DB URL: {db_display}")
        print()

        print("Object Storage Configuration:")
        print(f"  Object Store: {settings.object_store}")
        print()

        print("Authentication Configuration:")
        print(f"  OIDC Issuer: {settings.oidc_issuer_url}")
        print(f"  OIDC Audience: {settings.oidc_audience}")
        print("  JWT Key: ***")
        print()

        print("Event Bus Configuration:")
        print(f"  Event Bus URL: {settings.event_bus_url}")
        print()

        print("Environment Flags:")
        print(f"  Is Dev: {settings.is_dev}")
        print(f"  Is Staging: {settings.is_staging}")
        print(f"  Is Production: {settings.is_production}")
        print()

        print("=" * 60)
        print("Configuration loaded successfully!")
        print("=" * 60)

        return 0

    except ValueError as e:
        print(f"Configuration Error: {e}", file=sys.stderr)
        print("\nPlease ensure all required environment variables are set.", file=sys.stderr)
        print("See .env.example for the required configuration.", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
