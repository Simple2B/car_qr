from abc import abstractmethod, ABC
import os
import tomllib
import pathlib
from functools import lru_cache
from typing import ClassVar
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from flask import Flask


BASE_DIR = pathlib.Path(__file__).parent.absolute()
_project_toml = tomllib.loads((BASE_DIR / "pyproject.toml").read_text())
APP_VERSION = _project_toml["tool"]["poetry"]["version"]
APP_ENV = os.environ.get("APP_ENV", "development")


class BaseConfig(BaseSettings, ABC):
    """Base configuration."""

    @property
    @abstractmethod
    @abstractmethod
    def ENV(): ...

    APP_NAME: str = "Car's QR Code"
    APP_VERSION: str = APP_VERSION
    SECRET_KEY: str
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    WTF_CSRF_ENABLED: bool = False
    TIMEZONE: str = "EST"
    SHIPPING_PRICE: float = 0.0

    # Mail config
    MAIL_SERVER: str
    MAIL_PORT: int
    MAIL_USE_TLS: bool
    MAIL_USE_SSL: bool
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_DEFAULT_SENDER: str

    # Super admin
    ADMIN_FIRST_NAME: str
    ADMIN_LAST_NAME: str
    ADMIN_EMAIL: str
    ADMIN_PASSWORD: str

    # Pagination
    DEFAULT_PAGE_SIZE: int
    PAGE_LINKS_NUMBER: int

    # stripe env variables
    STRIPE_SUBSCRIPTION_SUCCESS_URL: str
    STRIPE_SUBSCRIPTION_CANCEL_URL: str

    STRIPE_SECRET_KEY: str
    ALPHANUMERIC_CODE_LENGTH: int
    LANDING_URL: str

    IMAGE_MAX_WIDTH: int = 512
    BASE_URL: str

    SUBSCRIPTIONS_EXPIRATION_CHECK_HOUR: int = 7
    DEVELOPERS_PASS: str | None = ""

    RECAPTCHA_PUBLIC_KEY: str = ""
    RECAPTCHA_PRIVATE_KEY: str = ""

    @staticmethod
    def configure(app: Flask):
        # Implement this method to do further configuration on your app.
        pass

    model_config = SettingsConfigDict(
        env_file=(
            ".env",
            "project.env",
        ),
        extra="ignore",
    )


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    # DEBUG: bool = True
    ENV: ClassVar[str] = "development"
    ALCHEMICAL_DATABASE_URL: str = Field(alias="DEVEL_DATABASE_URL")


class TestingConfig(BaseConfig):
    """Testing configuration."""

    ENV: ClassVar[str] = "testing"
    WTF_CSRF_ENABLED: bool = False
    TESTING: bool = True
    PRESERVE_CONTEXT_ON_EXCEPTION: bool = False
    ALCHEMICAL_DATABASE_URL: str = "sqlite:///" + os.path.join(
        BASE_DIR, "database-test.sqlite3"
    )


class ProductionConfig(BaseConfig):
    """Production configuration."""

    ENV: ClassVar[str] = "production"
    ALCHEMICAL_DATABASE_URL: str = Field(alias="DATABASE_URL")
    WTF_CSRF_ENABLED: bool = True


@lru_cache
def config(
    name=DevelopmentConfig.ENV,
) -> DevelopmentConfig | TestingConfig | ProductionConfig:
    CONF_MAP = {}

    for conf in (TestingConfig, DevelopmentConfig, ProductionConfig):
        CONF_MAP[conf.ENV] = conf

    return CONF_MAP[name]()
