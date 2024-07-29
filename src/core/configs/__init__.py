from src.core.configs.general import GeneralSettings
from src.core.configs.database import PostgresSettings
from src.core.configs.telegram import TelegramSettings


class Settings(
    GeneralSettings,
    PostgresSettings,
    TelegramSettings,
):
    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
