from extensions import db
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default="customer")
    bookings = db.relationship("Booking", backref="user", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.password,
            "role": self.role,
        }
class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(100))
    duration = db.Column(db.String(20))
    description = db.Column(db.Text)
    poster_url = db.Column(db.String(255))
    screenings = db.relationship("Screening", backref="movie", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "genre": self.genre,
            "duration": self.duration,
            "description": self.description,
            "poster_url": self.poster_url
        }

class Hall(db.Model):
    __tablename__ = "halls"
    id = db.Column(db.Integer, primary_key=True)
    hall_name = db.Column(db.String(50), nullable=False)
    screen_type = db.Column(db.String(50), nullable=False)
    screenings = db.relationship("Screening", backref="hall", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "hall_name": self.hall_name,
            "screen_type": self.screen_type,
        }

class Screening(db.Model):
    __tablename__ = "screenings"
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"))
    hall_id = db.Column(db.Integer, db.ForeignKey("halls.id"))
    date = db.Column(db.String(20))
    time = db.Column(db.String(20))
    available_seats = db.Column(db.Integer)
    bookings = db.relationship("Booking", backref="screening", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "movie_id": self.movie_id,
            "hall_id": self.hall_id,
            "date": self.date,
            "time": self.time,
            "available_seats": self.available_seats,
        }

class Booking(db.Model):
    __tablename__ = "bookings"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    screening_id = db.Column(db.Integer, db.ForeignKey("screenings.id"))
    number_of_tickets = db.Column(db.Integer)
    booking_status = db.Column(db.String(30))
    booking_date = db.Column(db.String(30))
    tickets = db.relationship("Ticket", backref="booking", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "screening_id": self.screening_id,
            "number_of_tickets": self.number_of_tickets,
            "booking_status": self.booking_status,
            "booking_date": self.booking_date,
        }

class Ticket(db.Model):
    __tablename__ = "tickets"
    id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(db.Integer, db.ForeignKey("bookings.id"))
    hall_id = db.Column(db.Integer, db.ForeignKey("halls.id"))
    ticket_status = db.Column(db.String(30))

    def to_dict(self):
        return {
            "id": self.id,
            "booking_id": self.booking_id,
            "hall_id": self.hall_id,
            "ticket_status": self.ticket_status,
        }
