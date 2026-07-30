from flask import Flask
from flask_cors import CORS
from config import Config
from extensions import db, migrate
from models import Movie, Screening, Booking, User
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

#@app.route("/bookings", methods=["POST"])
#def get_booking():
    #data = request.get_json()
    #booking = Booking(user_name = data["user_name"],
    #screening_id=data["screening_id"], seats=data["seats"])
    #db.session.add(booking)
    #db.session.commit()
    #return jsonify(booking.to_dict()), 201

@app.route("/bookings", methods=["POST"])
def create_booking():
    data = request.get_json()
    booking = Booking(user_id=data["user_id"],
                      screening_id=data["screening_id"],
                      number_of_tickets=data["number_of_tickets"],
                      booking_status=data["booking_status"],
                      booking_date=data["booking_date"])

    db.session.add(booking)
    db.session.commit()

    return jsonify(booking.to_dict()), 201

@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

@app.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user.to_dict()), 200

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    user = User(
        first_name=data["first_name"],
        last_name=data["last_name"],
        email=data["email"],
        password=data["password"],
        role=data.get("role", "customer")
    )
    db.session.add(user)
    db.session.commit()

    return jsonify(user.to_dict()), 201

@app.route("/users/<int:id>", methods=["PATCH"])
def update_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    user.first_name = data.get("first_name", user.first_name)
    user.last_name = data.get("last_name", user.last_name)
    user.email = data.get("email", user.email)
    user.password = data.get("password", user.password)
    user.role = data.get("role", user.role)

    db.session.commit()

    return jsonify(user.to_dict()), 200

@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)