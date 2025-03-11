# app.py
# Example: https://my-physics-web-app-7x-76cd3197c2e6.herokuapp.com/

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from models import db, Formula  # Import from models.py (NO redefinition)

app = Flask(__name__)

# Connect to Heroku PostgreSQL database
DATABASE_URL = os.environ.get("DATABASE_URL")

# Fix for Heroku PostgreSQL URLs (Heroku uses `postgres://`, but SQLAlchemy requires `postgresql://`)
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize db with app (NO reinitialization)
db.init_app(app)

@app.route("/")
def home():
    formulas = Formula.query.all()  # Fetch all formulas from DB
    return render_template("index.html", formulas=formulas)

if __name__ == "__main__":
    # Auto-create tables inside app context
    with app.app_context():
        db.create_all()
    app.run(debug=True)
