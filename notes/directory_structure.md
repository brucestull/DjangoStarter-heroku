# Project Directory Structure

* `tree /f /a`:  
    ```
        PS C:\Users\Bruce\Programming\totally-new-heroku-app-name> tree /f /a
        Folder PATH listing for volume OS
        Volume serial number is CC00-DD12
        C:.
        |   .gitignore
        |   LICENSE
        |   manage.py
        |   Pipfile
        |   Pipfile.lock
        |   Procfile
        |   README.md
        |
        +---my_current_project
        |   |   asgi.py
        |   |   urls.py
        |   |   wsgi.py
        |   |   __init__.py
        |   |
        |   \---settings
        |           common.py
        |           development.py
        |           production.py
        |
        +---notes
        |       add_database_settings_to_config_vars.md
        |       add_django_settings_module_to_config_vars.md
        |       add_secret_key_to_config_vars.md
        |       01_create_repository_from_template.md
        |       create_empty_remote_repo_push_existing_application.md
        |       create_heroku_application_server_instance.md
        |       directory_structure.md
        |       modify_allowed_hosts.md
        |       provision_database_server_instance.md
        |       push_to_heroku_and_createsuperuser.md
        |       02_run_application_locally.md
        |
        +---templates
        |   |   base.html
        |   |   home.html
        |   |
        |   \---registration
        |           login.html
        |           signup.html
        |
        \---users
            |   admin.py
            |   apps.py
            |   forms.py
            |   models.py
            |   tests.py
            |   urls.py
            |   views.py
            |   __init__.py
            |
            \---migrations
                    __init__.py
    ```


## Links:
[README.md](../README.md)
