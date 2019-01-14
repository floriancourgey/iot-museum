![](/docs/splash.jpg)

![](/museum/static/iot-museumx64.png) IoT Museum by [floriancourgey.com](https://floriancourgey.com?ref=iot-museum)
 &nbsp;[![Build Status](https://travis-ci.com/floriancourgey/iot-museum.svg?branch=master)](https://travis-ci.com/floriancourgey/iot-museum)
 
# IoT Museum
Display random artworks on any screen. Meant to be used with a Raspberry Pi linked to a monitor for an in-house museum.

*Demo available at https://floriancourgey.github.io/iot-museum.*

## General instructions
- Make sure to have python 3 installed. You can get it from https://www.python.org/downloads/. Check the installation with `python --version` in a terminal:
```bash
$ python --version
Python 3.7.0
```
- Download the sources (on github, "Clone or download" > "Download ZIP").
- Extract
- Open a terminal in the extracted folder
- Follow instructions below, depending on your system:

### Windows instructions
```bash
> pip install -r requirements.txt
> python manage.py runserver
```

- Open up a browser and go to `http://localhost:8000`

### Linux, Mac instructions
```bash
$ pip3 install -r requirements.txt
$ python3 manage.py runserver
```

- Open up a browser and go to `http://localhost:8000`

## Django management commands
```bash
$ manage.py makemigrations # creates .py files
$ manage.py migrate # execute migrations to db
$ manage.py crawler_rmngp # starts crawler
```

## Config
Edit `settings.py` and `.env`.

## Project overview
- Project structure
```python
- settings.py # project-wide settings
- museum/ # hosts the CSS+JS files
  - management/ # crawlers as Django commands
  - migrations/ # db updates
  - static/ # static CSS+JS files
  - templates/ # html
  - models.py # entity definition
  - views.py # controller
```

- Server overview
```python
/ # displays the main page with the artwork and a call every 5 sec to /next
/next # fetches a random artwork and display it as a JSON response
/reset # reset all timesPlayed to 0
```

## Access db via web Admin
Go to http://localhost:8000/admin and connect with admin/admin.

## Access db via GUI
Download [Sqlectron GUI](https://sqlectron.github.io/) and use the .db filepath as the "Initial Database":

![Sqlectron configuration](/docs/sqlectron-configuration.jpg)

## Flask vs Django
Django is better for:
- SQLite migration (unable to easily edit a column with Flask)
- Models accessible easily in Django Commands (similar to Symfony Commands)
- Admin interface on /admin
- Lighter ORM syntax
