from my_current_project.settings.common import *

import os


DEBUG = False


ALLOWED_HOSTS = ['django-custom-user-starter.herokuapp.com']


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd3tigpb1ih3690',
        'HOST': 'ec2-44-195-169-163.compute-1.amazonaws.com',
        'PORT': 5432,
        'USER': 'xusrikgdganklq',
        'PASSWORD': 'e64d5782c1878b15f9eedb77282f79cd73be28b104f22724eac744513f8669bf',
    }
}


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