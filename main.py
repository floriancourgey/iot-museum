#!/usr/bin/env python3
import random
from flask import Flask, render_template, jsonify
from config import config
from models import app, db, Artwork

numberOfArtworks = db.session.query(Artwork).count()

@app.route('/')
def index():
    return render_template('index.html', numberOfArtworks=numberOfArtworks)
@app.route('/next')
def next():
    offset = random.randint(0, numberOfArtworks-1)
    artwork = db.session.query(Artwork).limit(1).offset(offset).first().as_dict()
    # artworks[nextIndex]['played'] += 1
    return jsonify(artwork)
@app.route('/get/<int:id>')
def get():
    pass

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=config['app']['server_port'])
