import os

from config.settings.common import *  # noqa: F403, F401

MIDDLEWARE = MIDDLEWARE + ["whitenoise.middleware.WhiteNoiseMiddleware"]  # noqa: F405
