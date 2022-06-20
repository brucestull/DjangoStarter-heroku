# Modify Some Final Production Settings

## Resources:
* [Heroku](https://www.heroku.com/)
* [Deploy a Django App to Heroku - Video - Pretty Printed](https://www.youtube.com/watch?v=GMbVzl_aLxM)


## Process:
1. Get production database settings. Use the following commands to get the production database settings. Use local terminal.
    1. Log in to Heroku if not already logged in:  
    `heroku login`
    1. Start django shell:  
    `heroku run python manage.py shell`
    1. Investigate the value of `DEBUG`. It should be "False". If it is not "False" we may need to troubleshoot:  
    `print(s.DEBUG)`
    1. Investigate the django `SECRET_KEY`. It should be the same value user saved in Heroku Config Vars:  
    `print(s.SECRET_KEY)`
    1. Now, we are going to print the database settings. Save this information somewhere since we will need it later. In particular, we will need `NAME`, `USER`, `PASSWORD`, `HOST`, and `PORT`:  
    `print(s.DATABASES)`
        * Sample output:
            ```
            {
                "default": {
                    "NAME": "d7f6bli4ieugcn",
                    "USER": "wkuctbopkbukbe",
                    "PASSWORD": "f0fc47a2ac3078c983e63d5c746ac5b40276bf8308a80b18e818d51d107581e7",
                    "HOST": "ec2-34-200-35-222.compute-1.amazonaws.com",
                    "PORT": 5432,
                    "CONN_MAX_AGE": 600,
                    "OPTIONS": {"sslmode": "require"},
                    "ENGINE": "django.db.backends.postgresql_psycopg2",
                    "ATOMIC_REQUESTS": "False",
                    "AUTOCOMMIT": "True",
                    "TIME_ZONE": "None",
                    "TEST": {
                        "CHARSET": "None",
                        "COLLATION": "None",
                        "MIGRATE": "True",
                        "MIRROR": "None",
                        "NAME": "None"
                    }
                }
            }
            ```





## Links:
[README.md](../README.md)