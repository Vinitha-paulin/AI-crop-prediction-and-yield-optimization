from flask import Flask, render_template, request, redirect, url_for, session
import joblib
import numpy as np
import os
import webbrowser
import csv
from datetime import datetime

app = Flask(__name__)
app.secret_key = "secret123"

USER_FILE = "users.txt"
HISTORY_FILE = "data/prediction_history.csv"

# ------------------ LOAD MODELS ------------------
base_dir = os.path.dirname(os.path.abspath(__file__))

# Crop Recommendation Model
crop_model_path = os.path.join(base_dir, "..", "model", "crop_model.pkl")
crop_model = joblib.load(crop_model_path)

# Yield Prediction Model
yield_model_path = os.path.join(base_dir, "..", "model", "yield_model.pkl")
yield_model = joblib.load(yield_model_path)

# ------------------ CREATE HISTORY FILE ------------------
if not os.path.exists("data"):
    os.makedirs("data")

if not os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "username",
            "temperature",
            "humidity",
            "rainfall",
            "soil",
            "prediction",
            "date"
        ])

# ------------------ LOGIN ------------------
@app.route("/", methods=["GET", "POST"])
def login():
    message = ""

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if not os.path.exists(USER_FILE):
            message = "You didn't register. Please register first."
            return render_template("login.html", message=message)

        with open(USER_FILE, "r") as f:
            users = f.readlines()

        for user in users:
            u, p = user.strip().split(",")
            if u == username and p == password:
                session["user"] = username
                return redirect(url_for("dashboard"))

        message = "Invalid username or password"

    return render_template("login.html", message=message)

# ------------------ REGISTER ------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    message = ""

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        with open(USER_FILE, "a") as f:
            f.write(f"{username},{password}\n")

        message = "Registered successfully! Now login."

    return render_template("register.html", message=message)

# ------------------ DASHBOARD ------------------
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    today = datetime.now().strftime("%d-%m-%Y")

    return render_template(
        "dashboard.html",
        current_date=today
    )


# ------------------ YIELD PAGE ------------------
@app.route("/yield")
def yield_page():
    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("yield.html")


# ------------------ RECOMMEND PAGE ------------------
@app.route("/recommend_page")
def recommend_page():
    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("recommend.html")
# ------------------ YIELD PREDICTION ------------------
@app.route("/predict", methods=["POST"])
def predict():
    if "user" not in session:
        return redirect(url_for("login"))

    # Get input values
    temperature = float(request.form["temperature"])
    humidity = float(request.form["humidity"])
    rainfall = float(request.form["rainfall"])
    soil_moisture = float(request.form["soil_moisture"])

    # Prepare input
    input_data = np.array([[temperature, humidity, rainfall, soil_moisture]])

    # Predict yield
    prediction = yield_model.predict(input_data)
    result = round(prediction[0], 2)

    # Save history
    username = session.get("user")

    with open(HISTORY_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            username,
            temperature,
            humidity,
            rainfall,
            soil_moisture,
            result,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ])

    return render_template(
        "yield.html",
        prediction=result,
        temperature=temperature,
        humidity=humidity,
        rainfall=rainfall,
        soil_moisture=soil_moisture
    )
# ------------------ CROP RECOMMENDATION ------------------
@app.route("/recommend", methods=["POST"])
def recommend():
    if "user" not in session:
        return redirect(url_for("login"))

    N = float(request.form["N"])
    P = float(request.form["P"])
    K = float(request.form["K"])
    temperature = float(request.form["temperature"])
    humidity = float(request.form["humidity"])
    rainfall = float(request.form["rainfall"])

    input_data = np.array([[N, P, K, temperature, humidity, rainfall]])

    prediction = crop_model.predict(input_data)

    return render_template("recommend.html", crop=prediction[0])
# ------------------ HISTORY ------------------
@app.route("/history")
def history():
    if "user" not in session:
        return redirect(url_for("login"))

    history_data = []

    with open(HISTORY_FILE, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if row[0] == session.get("user"):
                history_data.append(row)

    return render_template("history.html", history=history_data)


# ------------------ LOGOUT ------------------
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


# ------------------ RUN ------------------
if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True)