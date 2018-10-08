# Flask-RESTful-example 

## Project Structure

```bash
Flask-RESTful-example
├── Pipfile 
├── README.md
├── app
│   ├── __init__.py
│   ├── api 
│   │   ├── __init__.py
│   │   └── database.py # SQLAlchemey
│   ├── books # API model example (such as Model)
│   │   ├── __init__.py
│   │   ├── models.py # SQLAlchemy ORM 
│   │   └── views.py # Flask Resource (such as Controller)
│   ├── config.py # app config
│   └── log # log folder
├── docker-compose.yml
├── images
└── run.py
```

## How to run

```bash
docker-compose up -d
python run.py
```

## Preview

![preview](./images/preview.png)