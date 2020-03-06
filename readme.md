

##### [Replace the contents this README.MD file with the appropriate "Users manual" needed for the project]  
  
   
   
# Web Content - Django Template

## Introduction

> This page gives details concerning guiding principles and skeleton template required for developing Django web application. 

## Requirements
- #### Git and Github accounts
    Follow this installation guide [HERE](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) to install Git in your local machine. Additionally, direct to Github [sign up](https://github.com/join?source=header-home) page if you do not have the account. 
- #### Python(version>2.7 or >3.0)
- #### PIP
    Follow [official PIP link](https://pip.pypa.io/en/stable/installing/) for installation instruction. 
- ```
    pip install django
    ```
- ```
    pip install pipenv
    ```

     
## Installation

> Getting started with the Django Template: 
- To create a new Django project (make sure to change `project_name`)
    ```
    django-admin.py startproject --template=https://github.com/biobakery/django-web-template/archive/master.zip --extension=py,md,html,txt project_name
    ```
- cd to your project and install the development dependences
    ```
    pipenv install --dev
    ```
- If you need a database, edit the settings and create one with:
    ```
    pipenv run python manage.py migrate
    ```
- Once everything it's setup you can run the development server: [http://localhost:8000/](http://localhost:8000/)
    ```
    pipenv run python manage.py runserver
    ```

## Testing 

##### Running test cases: 
This Django template uses Pytest as the testing framework. To run your test cases: 
- Using command line
    ```
    python ./manage.py test
    ```
- Using VS code (Run all test cases)
    - Get the [django-test-runner](https://marketplace.visualstudio.com/items?itemName=Pachwenko.django-test-runner) extension for VS Code. 
   -    ```
        ctrl/cmd + d + a 
        ``` 

##### Generate HTML coverage report  
```
pytest --cov=. --cov-report=html
chromium htmlcov/index.html
```

##### Test for Deprecation Warnings
If you want to upgrade from Django 1.11 to Django 2.0 you need to make sure that there are no DeprecationWarnings:
```
PYTHONWARNINGS=all pytest
```

 or
```
python -Wall manage.py test
```


Browser Demo :
![](project_name/static/img/ss.png)
