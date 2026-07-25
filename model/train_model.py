import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
data = pd.read_csv("data/crop_data.csv")

print(data.columns)

 
X = data[['temperature','humidity','rainfall','soil_moisture']]
y = data['crop_yield']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "model/crop_model.pkl")

print("Model trained and saved!")