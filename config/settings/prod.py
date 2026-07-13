"""
Production settings.
"""

import os

from utils import get_database_config_variables

from .base import *  # noqa: F403

DEBUG = False

ALLOWED_HOSTS = [host for host in [os.getenv("THIS_HOST")] if host]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["SECRET_KEY"]

MIDDLEWARE = MIDDLEWARE.copy()  # noqa: F405
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

database_config_variables = get_database_config_variables(os.environ["DATABASE_URL"])
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": database_config_variables["DATABASE_NAME"],
        "HOST": database_config_variables["DATABASE_HOST"],
        "PORT": database_config_variables["DATABASE_PORT"],
        "USER": database_config_variables["DATABASE_USER"],
        "PASSWORD": database_config_variables["DATABASE_PASSWORD"],
    }
}

STATIC_ROOT = BASE_DIR / "staticfiles"  # noqa: F405
