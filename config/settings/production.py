import os

from config.settings.common import *

ALLOWED_HOSTS = ["django-starter-heroku-31869c6a140f.herokuapp.com"]


MIDDLEWARE = MIDDLEWARE + ["whitenoise.middleware.WhiteNoiseMiddleware"]


# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_ROOT = BASE_DIR / "staticfiles"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# Create a specific `SECRET_KEY` for production and use it in production only.
SECRET_KEY = os.environ.get("SECRET_KEY")

# To create a new `SECRET_KEY`:
"""
    python manage.py shell
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())
"""
