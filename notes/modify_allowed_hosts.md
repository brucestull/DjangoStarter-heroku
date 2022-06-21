# Modify ALLOWED_HOSTS

## Resources:

## Process:

1. Edit `ALLOWED_HOSTS` property in `production.py` to include the heroku application root domain:  
    `ALLOWED_HOSTS = ['totally-new-heroku-app-name.herokuapp.com']`

1. Git `add`, `commit`, and `push` to `origin`:
