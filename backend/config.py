from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    OPENROUTER_API_KEY: str = ""
    GROQ_API_KEY: str = ""

    BACKEND_HOST: str = "0.0.0.0"
    BACKEND_PORT: int = 8000

    ENVIRONMENT: str = "development"
    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()