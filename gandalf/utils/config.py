from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    TOKEN: str
    RULE_LINK: str
    LOGGING_LEVEL: str = "ERROR"
