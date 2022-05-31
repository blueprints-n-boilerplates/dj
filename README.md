# @blueprints-n-boilerplates/dj

> This repository is intended as a cookiecutter for Django projects.


## Technologies


1. Django 3.10.2 and Django REST

- Backend framework used to create APIs, and is the main technology used in this repository.

2. Sendgrid

- Used for sending transactional emails.

3. Twilio

- Used for SMS--sending verification codes, in particular.

4. Swagger UI

- Visual documentation of available APIs.

5. Docker

- For containerizing apps.

6. Pre-commit

- Framework for managing and maintaining multi-language pre-commit hooks.

7. Autoflake8

- Tool to automatically fix some issues reported by flake8. A fork from autoflake and is used to remove unused imports and unused variables.

8. Isort

- Utility / Library to sort Python imports.

9. Black

- Uncompromising Python code formatter.



## First steps before running the app

1. Create a virtual environment named `venv`

```shell
python3 -m venv venv
```

2. Set environment variable values.



3. Get inside the environment, upgrade pip and install the packages listed in requirements.

```shell
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements/development.txt
```

4. Create environment file based on environment mode, and change the values.

> For development mode, duplicate `environment/dev.template.env` and rename the duplicate file
to `environment/development.env`. 
> For staging mode, duplicate `environment/staging.template.env` and rename the
duplicate file to `environment/staging.env`. 
> For staging mode, duplicate `environment/production.template.env` and
rename the duplicate file to `environment/production.env`.

6. Up the server

If just using the terminal, run

```shell
python manage.py runserver
```

If using Pycharm IDE, refer `docs/pycharm.md` to read about creating Django server configurations.

5. Run migrations

```shell
python manage.py migrate
```

5. Create superuser

```shell
python manage.py createsuperuser
```

6. Happy hacking!


## Enabling pre-committing

Print sample config yaml file.

```shell
pre-commit sample-config > .pre-commit-config.yml
```

Install pre-commit

```shell
pre-commit install
```

Uninstall pre-commit

```shell
pre-commit uninstall
```


## Running tests

```shell
python manage.py test --pattern="tests_*.py"
```

### 1. Coverage

> Code coverage testing for Python.
> It measures code coverage, typically during test execution. 
> It uses the code analysis tools and tracing hooks provided in the Python standard library to determine which lines 
> are executable, and which have been executed.
> 

```shell
coverage run --omit='*/venv/*' manage.py test
coverage report  # get report
coverage html  # will generate an HTML report with a folder htmlcov/
```