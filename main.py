#!/usr/bin/env python3
from flask import Flask
from flask import render_template

app = Flask(__name__)

artworks = [
    {'url':'medium.jpg','author':'','title':'Isenheim Altarpiece'},
    {'url':'medium(1).jpg','author':'','title':'The Tête à Tête'},
    {'url':'medium(2).jpg','author':'','title':'La Grande Odalisque'},
    {'url':'medium(3).jpg','author':'','title':'Olympia'},
    {'url':'medium(4).jpg','author':'','title':'Le Berceau (The Cradle)'},
]

@app.route('/')
def index():
    return render_template('index.html',
        artworks=artworks
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
