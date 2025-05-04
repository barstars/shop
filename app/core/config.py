from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    DATABASE_URL_USERS: str
    DEBUG: bool = False

    class Config:
        env_file = ".env"

setting = Setting()
