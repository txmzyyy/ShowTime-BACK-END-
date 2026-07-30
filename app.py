from flask import Flask
from flask_cors import CORS
from config import Config
from extensions import db, migrate

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

if __name__ == "__main__":
    app.run(debug=True)