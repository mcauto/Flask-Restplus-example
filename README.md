# Flask-RESTful-example 

## Project Structure

```bash
Flask-RESTful-example
├── Pipfile
├── Pipfile.lock
├── README.md
├── app
│   ├── __init__.py
│   ├── api│   │   ├── README.md
│   │   ├── __init__.py
│   │   ├── resources
│   │   │   ├── README.md
│   │   │   └── todo.py
│   │   └── rpc
│   │       ├── README.md
│   │       └── __init__.py
│   ├── config.py
│   ├── constants.py
│   ├── database
│   │   ├── README.md
│   │   └── __init__.py
│   ├── log
│   │   ├── README.md
│   │   └── app.log
│   ├── models
│   │   ├── README.md
│   │   ├── __init__.py
│   │   └── todo.py
│   └── tests
│       ├── README.md
│       ├── __init__.py
│       └── test_.py
├── confs
│   ├── README.md
│   ├── database
│   │   ├── README.md
│   │   └── mysql
│   └── manager
│       ├── README.md
│       └── systemd
├── docker-compose.yml
├── images
│   └── preview.png
├── init_migration.sh
├── manage.py
└── migrations
```

## How to run

```bash
docker-compose up -d
pip3 install pipenv
pipenv shell
pipenv run pip install pip==18.0
pipenv install
python manage.py run
```

## how to test

```
python manage.py test
```

## Preview

![preview](./images/preview.png)
