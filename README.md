# ShowTime Backend API

A Flask REST API for the ShowTime Movie Booking System. The backend manages users, movies, screenings, and bookings while providing secure user authentication using JSON Web Tokens (JWT).

## Features

- User registration
- User login with JWT authentication
- Password hashing using Werkzeug
- CRUD operations for Users
- Read Movies
- Read Screenings
- Create and View Bookings
- MySQL database integration
- Flask-Migrate database migrations
- Environment variable configuration using `.env`

---

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-JWT-Extended
- Flask-CORS
- Werkzeug
- python-dotenv

---

## Project Structure

```
ShowTime-BACK-END/
│
├── app.py
├── config.py
├── extensions.py
├── models.py
├── migrations/
├── .env
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd ShowTime-BACK-END
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Linux/macOS

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

Example:

```env
DATABASE_URI=mysql+pymysql://username:password@localhost/showtime
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret_key
```

---

## Database Setup

Run the following commands:

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

---

## Running the Application

```bash
python app.py
```

The API will run on:

```
http://127.0.0.1:5000
```

---

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /login | User login |

### Users

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /users | Get all users |
| GET | /users/<id> | Get a single user |
| POST | /users | Register a new user |
| PATCH | /users/<id> | Update a user |
| DELETE | /users/<id> | Delete a user |

### Movies

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /movies | Get all movies |
| GET | /movies/<id> | Get one movie |

### Screenings

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /screenings | Get all screenings |

### Bookings

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /bookings | Get all bookings (JWT Required) |
| POST | /bookings | Create a booking (JWT Required) |

---

## Authentication

Protected endpoints require a JWT access token.
Include the token in the request header:
```
Authorization: Bearer <your_access_token>
```
---

## Testing

The API was tested using **Postman**.

Tests included:

- CRUD functionality
- Authentication
- Invalid IDs
- Delete operations
- JSON response validation