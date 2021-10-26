# {{cookiecutter.project_name}}
{{cookiecutter.project_description}}

# User Installation

```bash
pip install {{cookiecutter.project_name}} --index-url=https://packages.idmod.org/api/pypi/pypi-production/simple
```

## Pre-requisites
- Python 3.9 x64


# Development Environment Setup

When setting up your environment for the first time, you can use the following instructions

## Local Setup
1) Clone the business logic/UI repository:
   ```bash
   > git clone https://github.com/InstituteforDiseaseModeling/{{cookiecutter.repository_name}}

2) Create a virtualenv. On Windows, please use venv to create the environment
   `python -m venv {{cookiecutter.project_name}}-env`
   On Unix(Mac/Linux) you can use venv or virtualenv
3) Activate the virtualenv

4) If you are on windows, run `pip install py-make --upgrade --force-reinstall`
5) Then run `python ./.dev_scripts/bootstrap.py`. This will install all the tools. 
6) Run the app 
```
python main.py
```
**Note** If you're using Pycharm, and you're running the app in debug mode, you may encounter an error. This is due to the IDE itself. 
Install the latest version of py charm (2021.2.1 RC or latest). 
## Development Tips

There is a Makefile file available for most common development tasks. Here is a list of commands
```bash
clean       -   Clean up temproary files
setup-dev   -   Set up packages in dev mode 
```
On Windows, you can use `pymake` instead of `make`

## Container Setup
### using built in development server
```
docker-compose -f docker-compose.yml build
docker-compose -f docker-compose.yml up
```

### using gunicorn
```
docker-compose -f docker-compose.staging.yml build
docker-compose -f docker-compose.staging.yml up
```

#### Manually updating licenses file
If you install additional third party packages, the licenses file should reflect the change. 
To utilize the Makefile commands for updating license files run  
```
pymake licenses
```

#### Package release
You will need to set up Git Secrets for `PYPI_STAGING_USERNAME` and `PYPI_STAGING_PASSWORD`
