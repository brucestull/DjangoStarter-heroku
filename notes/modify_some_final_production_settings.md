# Modify Some Final Production Settings

## Resources:
* [Heroku](https://www.heroku.com/)
* [Deploy a Django App to Heroku - Video - Pretty Printed](https://www.youtube.com/watch?v=GMbVzl_aLxM)


## Process:
* NOTE: Heroku states in the datastore admin page that the "credentials are not permanent". I'll have to make a future guide on how to tell when that happens and how to update settings. I'm thinking that can be done by parsing the "Config Vars" `DATABASE_URL` but that is beyond the scope of current exercise.
1. Open Heroku application dashboard and click the "Heroku Postgres" link:

1. Select the "Settings" tab:

1. Click the "View Credentials..." button:

1. Note the provided values:

1. I save the provided values as Heroku "Config Vars" using the following mapping:
```
Host        -->>    DATABASE_HOST
Database    -->>    DATABASE_NAME
User        -->>    DATABASE_USER
Port        -->>    DATABASE_PORT
Password    -->>    DATABASE_PASSWORD
```

1. Save the database settings as Heroku "Config Vars" KEY-VALUE pairs:

## NOTE: The following steps are already done for the user. The steps are given here as information only.

1. Move the `ALLOWED_HOSTS` property from `common.py` and paste into `development.py` and `production.py`:
    1. The `ALLOWED_HOSTS` of `development.py` can maybe be left empty:  
        `ALLOWED_HOSTS = []`
    1. The `ALLOWED_HOSTS` of `production.py` needs to have the deployed server's address:  
        `ALLOWED_HOSTS = ['totally-new-heroku-app-name.herokuapp.com']`

1. Move the `DATABASES` property setting from `common.py` to `development.py`:
    * Move the following section:
        ```
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
        ```

1. Add an import of `os` at the top of `production.py`:
    ```
    import os
    ```

1. Create a `DATABASES` property in `production.py` and give it the following contents. These statements use `os` to get the database server values from "Config Vars"s environment variables. The `ENGINE` value instructs Heroku to use a `postgresql` database:
    ```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DATABASE_NAME'),
            'HOST': os.environ.get('DATABASE_HOST'),
            'PORT': os.environ.get('DATABASE_PORT'),
            'USER': os.environ.get('DATABASE_USER'),
            'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        }
    }
    ```

1. Add a `STATIC_ROOT` property to `production.py` to provide place for static files on the production server. I'm not yet sure why or how this it true. Will need to research this:
    ```
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    ```

1. Add `WhiteNoiseMiddleware` to the `MIDDLEWARE` property in `production.py`:
    ```
    MIDDLEWARE = MIDDLEWARE + ['whitenoise.middleware.WhiteNoiseMiddleware']
    ```

1. Remove the `django_on_heroku` import and reference from `common.py` since we have manually made the changes to settings which `django_on_heroku` provides:
    * Remove the following from `common.py`:
        ```
        import django_on_heroku
        django_on_heroku.settings(locals())
        ```

1. Verify application still works locally and in production.


## Links:
[README.md](../README.md)