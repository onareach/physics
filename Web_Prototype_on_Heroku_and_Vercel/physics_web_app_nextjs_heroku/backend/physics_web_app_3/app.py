# app.py
# This app.py was created in order to expose an API endpoint for
# Vercel Next.js to call

from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)

# Add the Vercel production URL to the allowed origins
CORS(app, origins=[
    "http://localhost:3000",  # Local development
    "https://physicsweb-qzhqw8vdi-david-longs-projects-14094a66.vercel.app"  # Deployed Vercel site
])

DATABASE_URL = os.environ.get("DATABASE_URL")

def get_formulas():
    conn = psycopg2.connect(DATABASE_URL, sslmode="require")
    cursor = conn.cursor()
    cursor.execute("SELECT id, formula_name, latex FROM formula;")
    formulas = cursor.fetchall()
    result = [{"id": row[0], "formula_name": row[1], "latex": row[2]} for row in formulas]
    cursor.close()
    conn.close()
    return result

@app.route('/api/formulas', methods=['GET'])
def fetch_formulas():
    try:
        formulas = get_formulas()
        return jsonify(formulas)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
