# Pycharm

## Creating Django Server Configuration

1. Open edit run/debug configurations dialog and click edit configurations.
2. Add new configuration and select `Django Server`.
3. `ctrl + alt + s` to open settings dialog. Look for `Django` under `Languages and Frameworks` and edit the following fields:

- Enable Django support
- Django project root
- Settings
- Manage script

### runserver for development mode

1. Edit the following fields

- Name
  - dev-runserver
- Custom run command
  - runserver
- Environment variables
  - PYTHONUNBUFFERED=1;DJANGO_SETTINGS_MODULE=config.settings;READ_DOT_ENV_FILE=True;ENV_FILE=/absolute/file/path/blueprints-n-boilerplates/dj/environments/development.env
- Python interpreter
- Working directory

### runserver for staging mode

- Name
  - staging-runserver
- Custom run command
  - runserver
- Environment variables
  - PYTHONUNBUFFERED=1;DJANGO_SETTINGS_MODULE=config.settings;READ_DOT_ENV_FILE=True;ENV_FILE=/absolute/file/path/blueprints-n-boilerplates/dj/environments/staging.env

### runserver for production mode

- Name
  - production-runserver
- Custom run command
  - runserver
- Environment variables
  - PYTHONUNBUFFERED=1;DJANGO_SETTINGS_MODULE=config.settings;READ_DOT_ENV_FILE=True;ENV_FILE=/absolute/file/path/blueprints-n-boilerplates/dj/environments/production.env

### terminal environment variables

1. `ctrl + alt + s` to open settings dialog and select `Tools > Terminal`.
2. Paste the environment variables.

### migrate

> Personally, I do not recommend creating a server config for applying Django migrations.
> There might be a specific sequence of migrations you need to apply for your interconnected apps and this might cause some errors.
> Run migrations only on terminal.
> Refer to the sample command below.

```shell
python manage.py migrate appname 003_migration
``` 

# 
