# Add Properties to Heroku Config Vars

## Resources:
* [Heroku](https://www.heroku.com/)
* [Deploy a Django App to Heroku - Pretty Printed](https://www.youtube.com/watch?v=GMbVzl_aLxM)

## Process:
1. Log in to Heroku and open the application dashboard:
    * My dashboard link:
        * https://dashboard.heroku.com/apps/totally-new-heroku-app-name
1. Open the "Settings" tab.
1. Click "Reveal Config Vars". We will be adding two "Config Vars".
1. First config var we will add is `DJANGO_SETTINGS_MODULE`. This is the dotted path from project root directory to project `production.py` file. But we will not include the `py` extension.
    * My example path:
    `my_current_project.settings.production`
    * So, the "KEY" is DJANGO_SETTINGS_MODULE
    * And the "VALUE" is my_current_project.settings.production
    * Click "Add" button.
1. Next config var is `SECRET_KEY`. We will generate this using Django shell.
1. Add `SECRET_KEY` as the "KEY".
1. In terminal session in root of repository, create a key and be prepared to copy it to Heroku application settings "Config Vars":
    * Start Django shell:
    `python manage.py shell`
    * Import `get_random_secret_key`:
    `from django.core.management.utils import get_random_secret_key`
    * Use `get_random_secret_key` to get a new key:
    `print(get_random_secret_key())`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\DjangoCustomUserStarter-archive> python manage.py shell
        Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
        Type "help", "copyright", "credits" or "license" for more information.
        (InteractiveConsole)
        >>> from django.core.management.utils import get_random_secret_key
        >>> print(get_random_secret_key())
        o%tz4dbxm42$q=-_vj89l3@+)uw37a4b4!jurgw9&%+x9_f^o8
        ```
1. Add the output string in previous step as the "VALUE".
1. Click the "Add" button.
1. Dyno may restart itself during this process so there may be no need to restart it manually.
1. Add user's repository as remote:
    * LINK-FOR-INSTRUCTIONS-TO-PUSH-LOCAL-TO-USER-REMOTE-REPOSITORY


## Links:
[README.md](..\README.md)