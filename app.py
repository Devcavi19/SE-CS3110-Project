from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="traffic_simulator"
)

@app.route("/")
def welcome():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM simulations ORDER BY created_at DESC")
    simulations = cursor.fetchall()
    return render_template("welcome.html", simulations=simulations)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        password = generate_password_hash(request.form["password"])  # Hash the password

        cursor = db.cursor()
        try:
            cursor.execute(
                "INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)",
                (first_name, last_name, email, password)
            )
            db.commit()
            return redirect(url_for("signin"))
        except mysql.connector.errors.IntegrityError:
            return "Email already exists. Please use a different email."

    return render_template("signup.html")

@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()

        if user and check_password_hash(user["password"], password):
            session["user_id"] = user["id"]
            session["user_name"] = f"{user['first_name']} {user['last_name']}"
            return redirect(url_for("welcome"))
        else:
            return "Invalid credentials. Please try again."

    return render_template("signin.html")

@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        name = session.get("user_name", request.form["name"])
        email = session.get("email", request.form["email"])
        message = request.form["message"]
        user_id = session.get("user_id")

        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO feedback (user_id, name, email, message) VALUES (%s, %s, %s, %s)",
            (user_id, name, email, message)
        )
        db.commit()
        return redirect(url_for("welcome"))

    return render_template("feedback.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("welcome"))

if __name__ == "__main__":
    app.run(debug=True)
