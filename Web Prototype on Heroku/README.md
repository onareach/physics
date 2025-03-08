# Physics Program Prototype Setup

## Overview of the Plan for the Prototype Physics Web App

**Framework:** Use Flask (a lightweight Python web framework) to create a web front-end instead of using the terminal.

**Database:** Store physics formulas in PostgreSQL, which is Heroku’s default database.

**Front-End UI:** Use HTML + Jinja (Flask’s built-in templating engine) to dynamically display formulas.

**Deployment:** Push everything to Heroku and run it as a live web app.

## Step 1: Set Up Your Local Development Environment

### Best Practice for Managing Git and Virtual Environments (VENV)

#### Recommended Project Structure
```
your_project/
│── venv_[project_name]/  # Virtual environment (ignored by Git)
│── app.py                # Your Flask application
│── models.py             # Database models
│── templates/            # Directory for templates used by Flask
│── templates/index.html  # index.html template (includes MathJax)
│── static/               # [optional] CSS, JS, Images
│── requirements.txt      # Dependencies (tracked by Git)
│── Procfile              # Heroku startup instructions (tracked by Git)
│── .gitignore            # Files/folders to ignore (including venv)
│── README.md             # Project documentation
│── config.py             # [optional] Configuration settings
│── .python-version       # Specifies version of Python the app runs
```

### Create Project Directory
Navigate to the directory location where you want to create the project directory:
```bash
mkdir [project_folder_name]
cd [project_folder_name]
```

### Create and Activate venv (macOS)
```bash
python3 -m venv [venv_name]
source ./[venv_name]/bin/activate
```

### Install Required Python Dependencies
Ensure you are inside the activated virtual environment before running:
```bash
pip install flask
pip install flask_sqlalchemy
pip install psycopg2-binary
pip install gunicorn
```

**Note:** You can install all of these packages with one `pip install` command, but installing them individually makes troubleshooting easier.

### Install Global Dependencies (MacOS)
**Install PostgreSQL (if not installed)**
```bash
brew install postgresql
```
**Verify PostgreSQL installation**
```bash
psql --version
```
**Install Heroku CLI**
```bash
brew install heroku
```
**Verify Installation**
```bash
heroku --version
```
If installed correctly, it will display the version number.

**Log into Heroku**
```bash
heroku login
```
This will open a web browser page where you can authenticate your account.

## Step 2: Define Your Database Model File (models.py)
Create a `models.py` file to store formulas in a PostgreSQL database:
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Formula(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    formula_name = db.Column(db.String(100), nullable=False)
    latex = db.Column(db.Text, nullable=False)

def __repr__(self):
    return f"<Formula {self.formula_name}>"
```

## Step 3: Create the Flask App File (app.py)
Create `app.py`:
```python
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from models import db, Formula

app = Flask(__name__)

# Fix the DATABASE_URL issue for Heroku
database_url = os.getenv("DATABASE_URL")
if database_url and database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

@app.route("/")
def home():
    formulas = Formula.query.all()
    return render_template("index.html", formulas=formulas)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

## Step 4: Create index.html Template
Create a `templates` directory:
```bash
mkdir templates
```
Inside `templates/`, create `index.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Physics Formulas</title>
    <script type="text/javascript" async
        src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script type="text/javascript" async
        src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>
    <h1>Physics Formulas</h1>
    <ul>
        {% for formula in formulas %}
            <li>{{ formula.formula_name }}: <span>$$ {{ formula.latex }} $$</span></li>
        {% endfor %}
    </ul>
    <script>
        window.onload = function() {
            MathJax.typeset();
        };
    </script>
</body>
</html>
```

## Step 5: Deploy to Heroku
### Prepare Git Repository
```bash
git init
git add .
git commit -m "Initial commit"
```
### Create `requirements.txt`
```bash
pip freeze > requirements.txt
```
### Create `Procfile`
```bash
echo "web: gunicorn app:app" > Procfile
```
### Create and Deploy to Heroku
```bash
heroku create my-physics-formula-viewer
heroku addons:create heroku-postgresql --app my-physics-formula-viewer
```
### Push to Heroku
```bash
git push heroku main
```
### Initialize the Database
```bash
heroku run python
```
Inside the Heroku shell, run:
```python
from app import db, app
with app.app_context():
    db.create_all()
```
## Step 6: Open the App
```bash
heroku open
```
You should now see your formulas displayed dynamically from the PostgreSQL database.

## Next Steps & Enhancements
- **Admin Panel for Editing Formulas** → Use Flask-WTF or Flask-Admin.
- **User Authentication** → Implement Flask-Login for user management.
- **Deploy a React/Vue Front-End** → Host front-end separately while using Heroku as an API.

