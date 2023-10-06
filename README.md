# Django Basic Library App

Follow the steps below to run and develop this project.

## Run the following command to create a virtual environment:

```bash
python -m venv .venv
```
## Run the following command to activate virtual environment:
```bash
.venv\Scripts\activate
```

## Run the following command to install project dependencies:

```bash
pip install -r requirements.txt
```

## Run the following command to create the database:

```bash
python manage.py makemigrations app
```

```bash
python manage.py migrate
```

# Run the following command to start the project:
## To run in a virtual environment;
```bash
python manage.py runserver
```

## To run with docker;
```bash
docker build -t django-library-app .   
```
    
```bash
docker run -p 8000:8000 django-library-app
```

## To run with docker-compose;
```bash
docker-compose up
```

You can view the application by going to `http://localhost:8000` in your browser.


