import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    DEBUG: bool = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "defaultsecretkey")
    
settings = Settings()
