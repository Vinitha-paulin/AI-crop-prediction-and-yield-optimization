import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv("Crop_recommendation.csv")

# Features and label
X = df[['N', 'P', 'K', 'temperature', 'humidity', 'rainfall']]
y = df['label']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
with open("model/crop_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved!")