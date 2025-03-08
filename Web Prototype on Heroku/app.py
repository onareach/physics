# app.py

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from models import db, Formula  # Import the models from models.py

app = Flask(__name__)

# Fix the DATABASE_URL issue for Heroku
database_url = os.getenv("DATABASE_URL")
if database_url and database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)  # Properly initialize the database

@app.route("/")
def home():
    formulas = Formula.query.all()  # Fetch all formulas from DB
    return render_template("index.html", formulas=formulas)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Ensures tables are created
    app.run(debug=True)
