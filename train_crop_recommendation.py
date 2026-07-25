import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
df = pd.read_csv("Crop_recommendation.csv")
# Features & label
X = df[['N','P','K','temperature','humidity','rainfall']]
y = df['label']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, "model/crop_recommendation_model.pkl")

print("Crop recommendation model trained!")