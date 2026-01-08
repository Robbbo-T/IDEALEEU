"""Example FastAPI application using IDEALEEU configuration.

This example demonstrates how to integrate the configuration module
with a FastAPI application for API services.
"""

from typing import Dict
from config import get_settings, Settings


# Example: Using FastAPI (if available)
try:
    from fastapi import FastAPI, Depends

    app = FastAPI(
        title="IDEALEEU API",
        description="Example API using centralized configuration",
        version="1.0.0",
    )

    @app.get("/")
    async def root() -> Dict[str, str]:
        """Root endpoint.

        Returns basic API information and operational status.
        This endpoint can be used for basic connectivity checks.

        Returns:
            Dict containing API name and operational status
        """
        return {"message": "IDEALEEU API", "status": "operational"}

    @app.get("/health")
    async def health_check(settings: Settings = Depends(get_settings)) -> Dict[str, str]:
        """Health check endpoint with environment information."""
        return {
            "status": "healthy",
            "environment": settings.env.value,
            "log_level": settings.log_level.value,
        }

    @app.get("/config")
    async def config_info(settings: Settings = Depends(get_settings)) -> Dict[str, str]:
        """Configuration information endpoint (non-sensitive data only)."""
        # Safely extract protocol from URLs
        try:
            object_store_type = (
                settings.object_store.split("://")[0]
                if "://" in settings.object_store
                else "unknown"
            )
        except Exception:
            object_store_type = "unknown"

        try:
            event_bus_type = (
                settings.event_bus_url.split("://")[0]
                if "://" in settings.event_bus_url
                else "unknown"
            )
        except Exception:
            event_bus_type = "unknown"

        return {
            "environment": settings.env.value,
            "log_level": settings.log_level.value,
            "object_store_type": object_store_type,
            "oidc_issuer": settings.oidc_issuer_url,
            "event_bus_type": event_bus_type,
            "is_production": settings.is_production,
        }

    if __name__ == "__main__":
        import uvicorn

        settings = get_settings()

        # Configure uvicorn based on environment
        uvicorn.run(
            "fastapi_example:app",
            host="0.0.0.0",
            port=8000,
            reload=settings.is_dev,
            log_level=settings.log_level.value,
        )

except ImportError:
    print("FastAPI not installed. This is just an example.")
    print("To run this example, install: pip install fastapi uvicorn")
    print("\nConfiguration can still be used without FastAPI:")

    settings = get_settings()
    print(f"\nEnvironment: {settings.env.value}")
    print(f"Log Level: {settings.log_level.value}")
    print(f"Database configured: {'Yes' if settings.db_url else 'No'}")
    print(f"Object store configured: {'Yes' if settings.object_store else 'No'}")
