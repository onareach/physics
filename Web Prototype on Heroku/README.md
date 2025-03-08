# README.md

# Physics Program Prototype

## Overview
This project is a prototype web application for viewing and managing physics formulas. It uses **Flask** as the backend framework, **PostgreSQL** as the database, and **Jinja** for templating. The app is deployed on **Heroku**.

## Features
- Store physics formulas in a PostgreSQL database.
- View formulas dynamically using MathJax for proper LaTeX rendering.
- Flask-based backend with SQLAlchemy for database management.
- Deployment on Heroku with **Gunicorn** as the production server.

## Project Structure
```
your_project/
│── venv/               # Virtual environment (ignored by Git)
│── app.py              # Flask application
│── models.py           # Database models
│── templates/          # HTML templates
│── static/             # [Optional] CSS, JS, Images
│── requirements.txt    # Dependencies
│── Procfile            # Heroku startup instructions
│── .gitignore          # Files to ignore in Git
│── README.md           # Project documentation
│── config.py           # [Optional] Configuration settings
│── .python-version     # Specifies Python version
```

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/physics-program-prototype.git
cd physics-program-prototype
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate    # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up the database
```bash
flask db upgrade
```

### 5. Run the application locally
```bash
flask run
```

The app will be accessible at `http://127.0.0.1:5000/`.

## Deploying to Heroku
### 1. Log in to Heroku
```bash
heroku login
```

### 2. Create a Heroku app
```bash
heroku create my-physics-formula-viewer
```

### 3. Add PostgreSQL
```bash
heroku addons:create heroku-postgresql --app my-physics-formula-viewer
```

### 4. Deploy the app
```bash
git push heroku main
```

### 5. Initialize the database on Heroku
```bash
heroku run python
```
Then, inside the Heroku shell:
```python
from app import db, app
with app.app_context():
    db.create_all()
```

### 6. Open the live app
```bash
heroku open
```

## License
This project is licensed under the **MIT License**. See `LICENSE` for details.

---

# LICENSE (MIT)

MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

