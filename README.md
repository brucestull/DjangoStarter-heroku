# DjangoStarter-Heroku

> A Django starter template featuring a custom user model, auto-generated admin docs, separate DEV/PROD settings, pipenv, and Heroku support.

---

## Table of Contents

1. [Features](#features)  
2. [Prerequisites](#prerequisites)  
3. [Getting Started](#getting-started)  
   1. [Clone the Repository](#clone-the-repository)  
   2. [Install Dependencies](#install-dependencies)  
   3. [Configure Environment Variables](#configure-environment-variables)  
   4. [Run Locally](#run-locally)  
4. [Project Structure](#project-structure)  
5. [Running Tests](#running-tests)  
6. [Deployment to Heroku](#deployment-to-heroku)  
7. [Contributing](#contributing)  
8. [License](#license)  
9. [Acknowledgments](#acknowledgments)  

---

## Features

- **Custom User model**  
- **Django admin documentation generator** (admindocs)  
- **Separate** `DEV` and `PROD` settings modules  
- **Pipenv** for virtual environment and dependency management  
- **Heroku** Procfile and recommended config vars  

---

## Prerequisites

- **Python 3.11+** installed ([download](https://www.python.org/downloads/))  
- **Pipenv** installed (`pip install --user pipenv` or `pip install pipenv`)  
- **Git** installed ([download](https://git-scm.com/downloads))  
- **Heroku CLI** installed ([install guide](https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli))  
- A **Heroku** account ([signup](https://www.heroku.com/))  
- Familiarity with terminal / PowerShell commands  

---

## Getting Started

### 1. Fork the Repository

1. Go to the upstream repo: https://github.com/brucestull/DjangoStarter-heroku  
2. Click the **Fork** button in the top-right to create your own copy under your GitHub account.  

Once it’s forked, clone your fork:

```bash
git clone https://github.com/<your-username>/DjangoStarter-heroku.git
cd DjangoStarter-heroku
```


### 2. Install Dependencies

```bash
pipenv install --dev
pipenv shell
```

### 3. Configure Environment Variables

Create a `.env` file in the project root (or set config vars in Heroku):

```dotenv
# .env (DEV)
DJANGO_SETTINGS_MODULE=project.settings.dev
SECRET_KEY=your-development-secret-key
DATABASE_URL=sqlite:///db.sqlite3
```

**TODO:** Add any other environment variables your project requires (e.g. email creds, third-party API keys).

### 4. Run Locally

```bash
# apply migrations
python manage.py migrate

# create a superuser
python manage.py createsuperuser

# run the dev server
python manage.py runserver
```

Visit [http://localhost:8000](http://localhost:8000) and the admin docs at [http://localhost:8000/admin/doc/](http://localhost:8000/admin/doc/).

---

## Project Structure

```
DjangoStarter-heroku/
├── LICENSE
├── Pipfile				# Pipenv dependency file
├── Pipfile.lock		# Pipenv lock file
├── Procfile			# Heroku process file
├── README.md
├── accounts/			# Custom user model app
├── config/				# Django project configuration and settings
├── manage.py
├── notes/				# Notes and guides for setup
├── templates/			# HTML templates
└── utils.py			# Utility functions
```

**TODO:** Update this diagram if you add more apps or change directories.

---

## Running Tests

```bash
# inside pipenv shell
python manage.py test
```

**TODO:** Describe any test coverage requirements or specific test commands (e.g., `coverage run`, `flake8`).

---

## Deployment to Heroku

1. **Create Heroku app**

   ```bash
   heroku create your-app-name
   ```

2. **Set config vars**

   ```bash
   heroku config:set DJANGO_SETTINGS_MODULE=project.settings.prod
   heroku config:set SECRET_KEY=your-production-secret-key
   heroku config:set DATABASE_URL=your-database-url
   ```

3. **Push and migrate**

   ```bash
   git push heroku main
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   ```

4. **Visit your app**

   ```bash
   heroku open
   ```

**Process Notes:**
See [notes/01\_create\_repository\_from\_template.md](notes/01_create_repository_from_template.md) through [notes/09\_push\_to\_heroku\_and\_createsuperuser.md](notes/09_push_to_heroku_and_createsuperuser.md) for step-by-step details.

---

## Contributing

Contributions are welcome! Please:

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a pull request

**TODO:** Add any coding standards, linting rules, or testing requirements for contributors.

---

## License

Distributed under the [MIT License](LICENSE).
**TODO:** If you choose a different license, update this section.

---

## Acknowledgments

* **CustomUser** tutorial by Will Vincent:
  [https://learndjango.com/tutorials/django-custom-user-model](https://learndjango.com/tutorials/django-custom-user-model)
* **Django AdminDocs** reference:
  [https://docs.djangoproject.com/en/4.0/ref/contrib/admin/admindocs/](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/admindocs/)
* **DEV/PROD settings** guide from Thinkster:
  [https://thinkster.io/tutorials/configuring-django-settings-for-production](https://thinkster.io/tutorials/configuring-django-settings-for-production)

**TODO:** Add any other libraries, resources, or individuals you wish to thank.
