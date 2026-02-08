from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("bsoft.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS registrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone TEXT,
            course TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def register():
    return render_template("register.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    course = request.form["course"]

    conn = sqlite3.connect("bsoft.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO registrations (name, email, phone, course) VALUES (?, ?, ?, ?)",
        (name, email, phone, course)
    )
    conn.commit()
    conn.close()

    return render_template("success.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
