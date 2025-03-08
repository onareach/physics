# models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Formula(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    formula_name = db.Column(db.String(100), nullable=False)  # Correct column name
    latex = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Formula {self.formula_name}>"
