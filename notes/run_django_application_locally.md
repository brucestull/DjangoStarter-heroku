# Run application locally

## Assumptions:

* User has `python` installed.

## Notes:

* This example uses `python` to invoke interpreter. Other commands may possibly be used to invoke on other OSes (py, python3, etc). Use whichever is needed.

## Process:

### Clone repository:
* LINK-FOR-INSTRUCTIONS-TO-CLONE-REPO

### Start in root of repository: 
* `cd DjangoCustomUserStarter` 
* Sample current directory contents:  
    `ls`  
    ```
    Mode                 LastWriteTime         Length Name
    ----                 -------------         ------ ----
    d----          2022-05-15    15:50                my_current_project
    d----          2022-05-21    07:58                notes
    d----          2022-05-15    11:27                staticfiles
    d----          2022-05-21    07:58                templates
    d----          2022-05-15    11:49                users
    -a---          2022-04-02    23:57           1493 .gitignore
    -a---          2022-04-02    08:55          35823 LICENSE
    -a---          2022-05-15    15:50            708 manage.py
    -a---          2022-05-15    11:49            244 Pipfile
    -a---          2022-05-15    11:49           9066 Pipfile.lock
    -a---          2022-05-15    11:49            106 Procfile
    -a---          2022-05-21    07:58            979 README.md
    ```

### Install `pipenv`:  
- [ ] `pip install pipenv`  

### Create `pipenv` virtual environment:  
- [ ] `pipenv install`  

### Activate virtual environment:  
- [ ] `pipenv shell`  

### Perform Django database migrations:  
- [ ] `python manage.py migrate`  

### Create superuser:  
- [ ] `python manage.py createsuperuser`  

### Start server to run Django project:  
- [ ] `python manage.py runserver`

### Open browser to localhost url:  
- [ ] http://localhost:8000/

### Log in to the app using the superuser credentials created earlier. 

### Investigate features of application.

