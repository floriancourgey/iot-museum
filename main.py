#!/usr/bin/env python3
import random
from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
        artworks=getArtworks()
    )
@app.route('/next')
def next():
    artworks = getArtworks()
    nextIndex = random.randint(0, len(artworks)-1)
    artworks[nextIndex]['played'] += 1
    return json.dumps(artworks[nextIndex])
@app.route('/get/<int:id>')
def get():
    pass

def getArtworks():
    return [
        {'url':'medium.jpg','author':'','title':'Isenheim Altarpiece','played':0},
        {'url':'medium(1).jpg','author':'','title':'The Tête à Tête','played':0},
        {'url':'medium(2).jpg','author':'','title':'La Grande Odalisque','played':0},
        {'url':'medium(3).jpg','author':'','title':'Olympia','played':0},
        {'url':'medium(4).jpg','author':'','title':'Le Berceau (The Cradle)','played':0},
    ]

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
