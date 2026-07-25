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

# Yield Prediction Model (OLD)
model_path = os.path.join(base_dir, "..", "model", "crop_model.pkl")
model = joblib.load(model_path)

# Crop Recommendation Model (NEW)
crop_model_path = os.path.join(base_dir, "..", "model", "crop_model.pkl")
crop_model = joblib.load(crop_model_path)

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
    return render_template("index.html")

# ------------------ YIELD PREDICTION ------------------
@app.route("/predict", methods=["POST"])
def predict():
    if "user" not in session:
        return redirect(url_for("login"))

    temp = float(request.form["temperature"])
    humidity = float(request.form["humidity"])
    rainfall = float(request.form["rainfall"])
    soil = float(request.form["soil"])

    input_data = np.array([[temp, humidity, rainfall, soil]])
    prediction = model.predict(input_data)
    result = round(prediction[0], 2)

    # Save history
    username = session.get("user")

    with open(HISTORY_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            username,
            temp,
            humidity,
            rainfall,
            soil,
            result,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ])

    return render_template("index.html", result=result)

# ------------------ CROP RECOMMENDATION ------------------
@app.route("/recommend", methods=["POST"])
def recommend():
    if "user" not in session:
        return redirect(url_for("login"))

    temp = float(request.form["temperature"])
    humidity = float(request.form["humidity"])
    rainfall = float(request.form["rainfall"])

    input_data = [[temperature, humidity, rainfall, soil_moisture]]
    print(crop_model.n_features_in_)

    prediction = crop_model.predict(input_data)

    return render_template("index.html", crop=prediction[0])
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