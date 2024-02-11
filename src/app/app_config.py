from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

ALLOWED_ORIGINS = [origin.strip() for origin in os.getenv("ALLOWED_ORIGINS", "").split(",")]


@dataclass
class AppConfig:
    """
    Application configuration
    """
    PORT: int = int(os.getenv("APP_PORT", 5000))
    DEBUG: bool = bool(os.getenv("APP_DEBUG", False))
    HOST: str = os.getenv("APP_HOST", "0.0.0.0")


@dataclass
class CorsConfig:
    """
    CORS configuration
    """
    ORIGINS = ALLOWED_ORIGINS
