# Deploy to Heroku

## Resources:
* [Deploy to Heroku - Capstone guide](https://github.com/PdxCodeGuild/class_otter/blob/main/5%20Capstone/Heroku%20Deployment.md)
* [Deploy to Heroku - devcenter.heroku.com](https://devcenter.heroku.com/articles/git#for-a-new-heroku-app)

## Relevent commit:
* https://github.com/brucestull/DjangoCustomUserStarter/pull/7/commits/0f0bfbe1fb5efd97b09ec2c8ae5cc72621f17d06

## Steps:

1. Assumptions:  
    * Assumed Heroku CLI is installed. [Heroku CLI](https://devcenter.heroku.com/categories/command-line)
    * Application is already running locally in `pipenv` virtual environment.

1. Log in to Heroku in CLI:  
`heroku login`

1. **(Optional)** Check remote git repositories before Heroku app creation:  
`git remote -v`
    ```
    origin  https://github.com/brucestull/DjangoCustomUserStarter.git (fetch)
    origin  https://github.com/brucestull/DjangoCustomUserStarter.git (push)
    ```

1. Create the Heroku app, our app name is `django-custom-user-starter`:  
`heroku create django-custom-user-starter`  

1. **(Optional)** Note server locations for application deployment and Heroku git repository:  
    * https://django-custom-user-starter.herokuapp.com/
    * https://git.heroku.com/django-custom-user-starter.git

1. **(Optional)** Verify remote git repositories. There should be the existing repository and a new remote for Heroku **(NOTE: There are other ways to set up remotes with multiple remotes on one remote 'name' but we will has two separate named remotes for this exercise)**:
`git remote -v`
    ```
    heroku  https://git.heroku.com/django-custom-user-starter.git (fetch)
    heroku  https://git.heroku.com/django-custom-user-starter.git (push)
    origin  https://github.com/brucestull/DjangoCustomUserStarter.git (fetch)
    origin  https://github.com/brucestull/DjangoCustomUserStarter.git (push)
    ```

1. **(Optional)** View current installed packages:  
`pip list`
    ```
    Package    Version
    ---------- -------
    asgiref    3.5.0
    Django     3.2
    docutils   0.18.1
    pip        22.0.4
    pytz       2022.1
    setuptools 60.9.3
    sqlparse   0.4.2
    wheel      0.37.1
    ```

1. Install [django-on-heroku](https://pypi.org/project/django-on-heroku/) and [gunicorn](https://pypi.org/project/gunicorn/):  
`pipenv install django-on-heroku==1.1.2 gunicorn==20.1.0`

1. **(Optional)** View newly installed packages:  
`pip list`
    ```
    Package          Version
    ---------------- -------
    asgiref          3.5.1
    dj-database-url  0.5.0
    django-on-heroku 1.1.2
    gunicorn         20.1.0
    psycopg2-binary  2.9.3
    wheel            0.37.1
    whitenoise       6.1.0
    ```

1. Add import for `django_on_heroku` and call `django_on_heroku.settings` in `settings.py`:
    ```
    import django_on_heroku
    django_on_heroku.settings(locals())
    ```

1. Create `Procfile` in root of repo:  
    ```
    web: gunicorn my_current_project.wsgi
    release: python manage.py migrate users && python manage.py migrate
    ```

1. Git `add`:  
`git add <changed files>`

1. Git `commit`:  
`git commit -m "commit message"`

1. Git `push` to `origin`:  
`git push origin main`

1. Git `push` to `heroku` to initiate application deployment:  
`git push heroku main`

1. Create superuser on Heroku server:  
`heroku run python manage.py createsuperuser`

1. Verify deployment:  
    * https://django-custom-user-starter.herokuapp.com/