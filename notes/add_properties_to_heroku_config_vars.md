# Add Properties to Heroku Config Vars

## Resources:
* [Heroku](https://www.heroku.com/)
* [Deploy a Django App to Heroku - Video - Pretty Printed](https://www.youtube.com/watch?v=GMbVzl_aLxM)

## Process:

1. Log in to Heroku and open the dashboard for the application:
    * My dashboard link:
        * https://dashboard.heroku.com/apps/totally-new-heroku-app-name

1. Open the "Settings" tab:

1. Click "Reveal Config Vars":

1. Note the empty spaces where we will input the `KEY` and `VALUE` pairs for environment "Config Vars":

1. First config var we will add is `DJANGO_SETTINGS_MODULE`. This is the dotted path from project root directory to project `production.py` file. But we will not include the `py` extension. This value is used by `wsgi.py` and `manage.py` to set the production deployment to use the `production.py` settings:
    * My example slash path:  
    `my_current_project\settings\production`
    * My example dotted path:
    `my_current_project.settings.production`
    * So, the `KEY` is:  
    `DJANGO_SETTINGS_MODULE`
    * And the `VALUE` is:  
    `my_current_project.settings.production`

1. Click "Add" button:

1. Next config var is `SECRET_KEY`. We will generate this using Django shell.
    * In terminal session in root of repository, create a key and be prepared to copy it to Heroku application settings "Config Vars":
    
    1. Start Django shell:  
    `python manage.py shell`
    
    1. Import `get_random_secret_key`:  
    `from django.core.management.utils import get_random_secret_key`
    
    1. Use `get_random_secret_key` to get a new key:  
    `print(get_random_secret_key())`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\my-new-app-repository> python manage.py shell
        Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
        Type "help", "copyright", "credits" or "license" for more information.
        (InteractiveConsole)
        >>> from django.core.management.utils import get_random_secret_key
        >>> print(get_random_secret_key())
        oh%0+gz6)f0$=^y8y!p45+*y1pi($!x$wjc0own=5hi&j$-jmx
        >>> quit()
        ```

1. Add `SECRET_KEY` as the `KEY` and the output string in previous step as the `VALUE`:

1. Click the "Add" button.

1. Save the database settings as Heroku "Config Vars" KEY-VALUE pairs similar to how we added the other "Config Vars":
    * I save the provided values as Heroku "Config Vars" using the following mapping:
        ```
        Host        -->>    DATABASE_HOST
        Database    -->>    DATABASE_NAME
        User        -->>    DATABASE_USER
        Port        -->>    DATABASE_PORT
        Password    -->>    DATABASE_PASSWORD
        ```
    * Sample values, from earlier:
        ```
        Host        ec2-52-71-23-11.compute-1.amazonaws.com
        Database    d12en8ankbfql6
        User        fnsrzllkwjdrrf
        Port        5432
        Password    8c7ff88eb1c45aeccb61bf68d7540db7710e3c8adce41f8334b8f0f51aa534b4
        ```

1. [Modify Some Final Production Settings and Deploy to Heroku](modify_some_final_production_settings.md)

## Links:
[README.md](../README.md)
