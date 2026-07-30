from flask import Flask
from flask_cors import CORS
from config import Config
from extensions import db, migrate
from models import Movie, Screening, Booking
from flask import request, jsonify

app= Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate.init_app(app, db)
CORS(app)

import models

@app.route("/")
def home():
    return {
        "message": "Welcome to ShowTime"
    }

@app.route("/movies", methods=["GET"])
def get_movies():
    movies = Movie.query.all()
    return jsonify([movie.to_dict()for movie in movies])

@app.route("/movies/<int:id>", methods=["GET"])
def get_movie(id):
    movie = Movie.query.get_or_404()
    return jsonify([movie.to_dict()])

@app.route("/screenings", methods=["GET"])
def get_screenings():
    screenings = Screening.query.all()
    return jsonify([screening.to_dict() for screening in screenings])

@app.route("/bookings", methods=["POST"])
def get_booking():
    data = request.get_json()
    booking = Booking(user_name = data["user_name"],
    screening_id=data["screening_id"], seats=data["seats"])
    db.session.add(booking)
    db.session.commit()
    return jsonify(booking.to_dict()), 201

if __name__ == "__main__":
    app.run(debug=True)