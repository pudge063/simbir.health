from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_NAME: str
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PORT: str

    def get_connection():
        return 

    model_config = SettingsConfigDict(env_file=".env")

    

