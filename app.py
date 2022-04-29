from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask('name')
password = '12345'
PG_DSN = f'postgresql://asyncio:{password}@127.0.0.1:5432/asyncio'
app.config.from_mapping(SQLALCHEMY_DATABASE_URI=PG_DSN)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class HeroModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    films = db.Column(db.String(256))
    gender = db.Column(db.String(128))
    hair_color = db.Column(db.String)
    height = db.Column(db.Integer)
    homeworld = db.Column(db.String)
    mass = db.Column(db.Integer)
    name = db.Column(db.String)
    skin_color = db.Column(db.String)
    species = db.Column(db.String)
    starships = db.Column(db.String)
    vehicles = db.Column(db.String)

