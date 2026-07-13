"""
Development settings.
"""

import os

from .base import *  # noqa: F403

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# SECURITY WARNING: keep the secret key used in production secret!
# A default `SECRET_KEY` value is used here so that the project can be run
# locally, in development, without having to set an environment variable.
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-mm8cx0al6wo$$0hhv3&eevzsst9dbw&(5p$#9k(1rx%e@j+=$l",
)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # noqa: F405
    }
}
