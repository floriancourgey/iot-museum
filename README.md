# IoT Museum
Display random artworks on any screen. Meant to be used with a Raspberry Pi linked to a monitor for an in-house museum.

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
$ pip install -r requirements.txt
$ python main.py
```

### Linux, Mac instructions
```bash
$ pip3 install -r requirements.txt
$ chmod +x main.py
$ ./main.py
```

- Open up a browser and go to `http://localhost:5000`

## Config
Edit `config.yml`.

## Project overview
- Project structure
```python
- crawler-*.py # python crawlers to feed database with artworks
- main.py # starts the server on localhost:5000
- static/ # hosts the CSS+JS files
- templates/ # hosts the html template
```

- Server overview
```python
/ # displays the main page with the artwork and a call every 5 sec to /next
/ next # fetches a random artwork and display it as a JSON response
```

## Access db via GUI
Download [Sqlectron GUI](https://sqlectron.github.io/) and use the .db filepath as the "Initial Database":

![Sqlectron configuration](/docs/sqlectron-configuration.jpg)
