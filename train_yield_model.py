import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle
import os

# Load dataset
df = pd.read_csv("yield_data.csv")

# Features
X = df[['temperature', 'humidity', 'rainfall', 'area']]

# Target
y = df['yield']

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Create model folder if it doesn't exist
os.makedirs("model", exist_ok=True)

# Save model
with open("model/yield_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Yield Prediction Model trained successfully!")