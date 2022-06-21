# Provision Database Server

## Resources:
* https://dashboard.heroku.com/

## Process:

1. Open dashboard for the application we created:

1. Click the "Configure Add-ons" links:

1. Start search for "heroku postgres":

1. Click "Heroku Postgres" item:

1. Check order form and click "Submit Order Form" button:

1. Click "Heroku Postgres" line item link:

1. Select "Settings" tab:

1. Click "View Credentials..." button:

1. Take note of database server settings, we will need these values later:
    * Sample values:
        ```
        Host        ec2-52-71-23-11.compute-1.amazonaws.com
        Database    d12en8ankbfql6
        User        fnsrzllkwjdrrf
        Port        5432
        Password    8c7ff88eb1c45aeccb61bf68d7540db7710e3c8adce41f8334b8f0f51aa534b4
        ```

1. [Add Properties to Heroku Config Vars](add_properties_to_heroku_config_vars.md)

## Links:
[README.md](../README.md)