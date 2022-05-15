from my_current_project.settings.common import *


DEBUG = True


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# Create your own `SECRET_KEY` here for use in Development. Create a specific one for production only and use it in production only.
SECRET_KEY = "3)hq&x!awji5*(iw3ovzji^92as-nw57(m@7h#x^-c2wzu%qam"

# To create a new `SECRET_KEY`:
"""
    python .\manage.py shell
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())
"""