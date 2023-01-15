# 05 - Add DJANGO_SETTINGS_MODULE to Config Vars

## Resources

## Process

1. Log in to Heroku and open the dashboard for the application:
    * My dashboard link:
        * <https://dashboard.heroku.com/apps/totally-new-heroku-app-name>

1. Open the "Settings" tab:
![02_open_the_settings_tab](https://user-images.githubusercontent.com/47562501/207200024-a64261db-6def-47a9-aa7d-8a3dec7ffe3c.png)

1. Click "Reveal Config Vars":
![02_click_reveal_config_vars_button](https://user-images.githubusercontent.com/47562501/174794919-a0037f90-da9d-4878-8f5a-a1191d084f8c.png)

1. Note the empty spaces where we will input the `KEY` and `VALUE` pairs for environment "Config Vars":
![03_note_key_and_value_fields](https://user-images.githubusercontent.com/47562501/174794940-3e288522-39f5-4ca7-8b01-afaa5ef3312a.png)

1. First config var we will add is `DJANGO_SETTINGS_MODULE`. This is the dotted path from project root directory to project `production.py` file. But we will not include the `py` extension. This value is used by `wsgi.py` and `manage.py` to set the production deployment to use the `production.py` settings:
    * My absolute path:  
    `C:\Users\FlynntKnapp\Programming\my-local-repository\config\settings\production.py`
    * My example file slash path to `production.py`:  
    `config\settings\production.py`
    * My example dotted path:  
    `config.settings.production`
    * So, the `KEY` is:  
    `DJANGO_SETTINGS_MODULE`
    * And the `VALUE` is:  
    `config.settings.production`
![04_django_settings_module_entered](https://user-images.githubusercontent.com/47562501/174794977-931e5f9f-9c5d-4097-ab33-881184de6d9d.png)

1. Click "Add" button:
![05_click_add_button](https://user-images.githubusercontent.com/47562501/174795002-59dafe00-8764-49e8-8607-2fcabc7e33e2.png)

1. Proceed to [Add Django SECRET_KEY to Config Vars](06_add_secret_key_to_config_vars.md)

## Repository Links

[README.md](../README.md)
