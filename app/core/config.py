import os

from pydantic import Field
from pydantic_settings import BaseSettings


class DatabaseSettings(BaseSettings):
    db_host: str = Field("localhost", env="DB_HOST")
    db_port: int = Field(5432, env="DB_PORT")
    db_user: str = Field("user", env="DB_USER")
    db_name: str = Field("postgres", env="DB_NAME")
    db_pass: str = Field("password", env="DB_PASS")

    testing_host: str = Field("localhost", env="TESTING_HOST")
    testing_port: int = Field(5432, env="TESTING_PORT")
    testing_user: str = Field("user", env="TESTING_USER")
    testing_name: str = Field("postgres", env="TESTING_NAME")
    testing_pass: str = Field("password", env="TESTING_PASS")

    class Config:
        env_file = f"{os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))}/.env"  # noqa
        env_file_encoding = "utf-8"

    def get_db_url(self):
        return (
            f"postgresql+asyncpg://{self.db_user}:{self.db_pass}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )

    def get_testing_db_url(self):
        return (
            f"postgresql+asyncpg://{self.testing_user}:{self.testing_pass}"
            f"@{self.testing_host}:{self.testing_port}/{self.testing_name}"
        )


class Setting(BaseSettings):
    database: DatabaseSettings = DatabaseSettings()


settings = Setting()
