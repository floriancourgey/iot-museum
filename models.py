from config import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config['app']['sql_connection_string']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
app.app_context().push()
db.create_all()

class Artwork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(255))
    author = db.Column(db.String(255))
    timesPlayed = db.Column(db.Integer, nullable=False, default=0)
    def as_dict(self):
       return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
