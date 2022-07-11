# Django Starter with CustomUser, Django Documentation Generator, DEV-PROD settings, pipenv, and Heroku Procfile.


* NOTE: Author is using PowerShell for this guide.

## Features:
* Custom user model.
* Django admin documentation generator.
* Separate DEV and PROD settings.
* Pipfile included.
* Heroku Procfile included.
* [Project Directory Structure](notes/directory_structure.md)

## Assumptions:
* User has functioning [Python](https://www.python.org/downloads/) 3.10 installation.
* User has functioning [pipenv](https://pypi.org/project/pipenv/) installation.
* User has functioning [git](https://git-scm.com/downloads) installation.
* User is familiar with how to use terminal commands.
* User has [Heroku](https://www.heroku.com/) account.
* User had [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli) installed.

## Process:
1. [Clone DjangoCustomUserStarter Repository](notes/clone_django_custom_user_starter_repo.md) NOTE: Making a fork of this repo is better option. Documentation is in progress.
1. [Create Empty Remote GitHub Repository and Push Existing Application](notes/create_empty_remote_repo_push_existing_application.md)
1. [Run Application Locally](notes/run_application_locally.md)
1. [Create Heroku Application Server Instance](notes/create_heroku_application_server_instance.md)
1. [Provision Database Server Instance](notes/provision_database_server_instance.md)
1. [Add DJANGO_SETTINGS_MODULE to Config Vars](notes/add_django_settings_module_to_config_vars.md)
1. [Add Django SECRET_KEY to Config Vars](notes/add_secret_key_to_config_vars.md)
1. [Add Database Settings to Config Vars](notes/add_database_settings_to_config_vars.md)
1. [Modify ALLOWED_HOSTS](notes/modify_allowed_hosts.md)
1. [Push to Heroku and Create Superuser](notes/push_to_heroku_and_createsuperuser.md)

## Excellent resources, this project wouldn't have been possible without these:
* CustomUser method: [Django Best Practices: Custom User Model - Will Vincent - LearnDjango](https://learndjango.com/tutorials/django-custom-user-model)
* Docutils: [The Django admin documentation generator](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/admindocs/)
* DEV and PROD settings: [Configuring Django Settings for Production](https://thinkster.io/tutorials/configuring-django-settings-for-production)

## Links to this project's pages:
* DjangoCustomUserStarter [Production Deployment](https://django-custom-user-starter.herokuapp.com/)
* DjangoCustomUserStarter [Project Board](https://github.com/brucestull/DjangoCustomUserStarter/projects/1)
* DjangoCustomUserStarter [Repository](https://github.com/brucestull/DjangoCustomUserStarter)
