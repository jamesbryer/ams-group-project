import re
from application import db
from wtforms.validators import ValidationError
from datetime import datetime

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True, index=True)
    password = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True, index=True)
    bookings = db.relationship('Bookings', backref='user', lazy=True)

class PaymentDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_name = db.Column(db.String(30), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    card_number = db.Column(db.String(16), nullable=False, unique=True, index=True)
    expiry_date = db.Column(db.String(5), nullable=False)
    security_code = db.Column(db.String(3), nullable=False)

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False, unique=True, index=True)
    actors = db.Column(db.Integer, db.ForeignKey('actors.id'), nullable=False, index=True)
    director = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=False, index=True)

class Genres(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(30), nullable=False, unique=True, index=True)

class MovieGenres(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False, index=True)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=False, index=True)

class Actors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    actor = db.Column(db.String(30), nullable=False, unique=True, index=True)

class MovieActors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False, index=True)
    actor_id = db.Column(db.Integer, db.ForeignKey('actors.id'), nullable=False, index=True)


class Showings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False, index=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    seats = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    bookings = db.relationship('Bookings', backref='showing', lazy=True)

class Bookings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False, index=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    seat = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)

