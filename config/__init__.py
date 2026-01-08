"""IDEALEEU Configuration Module.

This module provides centralized configuration management for the IDEALEEU platform.
Environment variables are loaded and validated to ensure proper system operation.
"""

from .settings import Settings, get_settings

__all__ = ["Settings", "get_settings"]
