import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def init_db():
    """Initializes the database with a settings table."""
    with sqlite3.connect('wear_app.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_settings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                weight REAL,
                height REAL
            )
        ''')
        conn.commit()

init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/settings", methods=["GET", "POST"])
def settings():
    if request.method == "POST":
        weight_input = request.form.get("weight")
        height_input = request.form.get("height")

        with sqlite3.connect('wear_app.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO user_settings (weight, height) VALUES (?, ?)", 
                           (weight_input, height_input))
            conn.commit()
            
        return redirect(url_for('home'))

    return render_template("settings.html")
    
if __name__ == "__main__":
    app.run(debug=True)