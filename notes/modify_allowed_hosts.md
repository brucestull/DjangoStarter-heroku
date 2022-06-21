# Modify ALLOWED_HOSTS

## Resources:
* [Deploy a Django App to Heroku - Video - Pretty Printed](https://www.youtube.com/watch?v=GMbVzl_aLxM)

## Process:

1. Edit `ALLOWED_HOSTS` property in `production.py` to include the heroku application root domain:  
    `ALLOWED_HOSTS = ['totally-new-heroku-app-name.herokuapp.com']`

1. Git `add`, `commit`, and `push` to `origin`:

1. [Push to Heroku and Create Superuser](push_to_heroku_and_createsuperuser.md)

## Links:
[README.md](../README.md)