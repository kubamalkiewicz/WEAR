import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def init_db():
<<<<<<< HEAD
    """Creates the table if it doesn't exist."""
=======
    """Initializes the database with a settings table."""
>>>>>>> 02ce89a8799b1736e9c9ffdfc758eb995c10513a
    with sqlite3.connect('wear_app.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_settings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                weight REAL,
<<<<<<< HEAD
                height REAL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
=======
                height REAL
            )
        ''')
        conn.commit()

>>>>>>> 02ce89a8799b1736e9c9ffdfc758eb995c10513a
init_db()

@app.route("/")
def home():
    current_weight = None
    current_height = None

<<<<<<< HEAD
    with sqlite3.connect('wear_app.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT weight, height FROM user_settings ORDER BY id DESC LIMIT 1")
        data = cursor.fetchone()
        
        if data:
            current_weight = data[0]
            current_height = data[1]

    return render_template("index.html", weight=current_weight, height=current_height)

=======
>>>>>>> 02ce89a8799b1736e9c9ffdfc758eb995c10513a
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
            
<<<<<<< HEAD
        return redirect(url_for('stats'))
=======
        return redirect(url_for('home'))
>>>>>>> 02ce89a8799b1736e9c9ffdfc758eb995c10513a

    return render_template("settings.html")

@app.route("/stats")
def stats():
    history_data = []

    with sqlite3.connect('wear_app.db') as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user_settings ORDER BY id DESC")
        history_data = cursor.fetchall()

    return render_template("stats.html", history=history_data)

if __name__ == "__main__":
    app.run(debug=True)