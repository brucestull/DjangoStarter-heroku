from my_current_project.settings.common import *

import os


DEBUG = False

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# Create a specific `SECRET_KEY` for production and use it in production only.
SECRET_KEY = os.environ.get('SECRET_KEY')

# To create a new `SECRET_KEY`:
"""
    python .\manage.py shell
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())
"""