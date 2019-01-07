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
