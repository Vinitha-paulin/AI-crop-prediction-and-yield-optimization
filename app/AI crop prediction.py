from flask import Flask, render_template, request
import joblib
import numpy as np
import os
import webbrowser

app = Flask(__name__)

# Load model (correct path)
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, "..", "model", "crop_model.pkl")

model = joblib.load(model_path)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Prediction
@app.route("/predict", methods=["POST"])
def predict():
    temp = float(request.form["temperature"])
    humidity = float(request.form["humidity"])
    rainfall = float(request.form["rainfall"])
    soil = float(request.form["soil_moisture"])

    input_data = np.array([[temp, humidity, rainfall, soil]])

    prediction = model.predict(input_data)

    return f" Predicted Crop Yield: {round(prediction[0], 2)} tons/hectare"

# Auto open browser + run app
if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True)