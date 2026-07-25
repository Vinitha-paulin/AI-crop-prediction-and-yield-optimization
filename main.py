import pandas as pd
from sklearn.linear_model import LinearRegression

print("\n  AI Crop Yield Prediction System Started...\n") 


# Load Dataset

try:
    dataset = pd.read_csv("data/crop_data.csv")
    print(" Dataset loaded successfully") 
except FileNotFoundError:
    print(" Dataset file not found. Check data folder.") 
    exit()


# Select Input Features

features = dataset[
    ["temperature", "humidity", "rainfall", "soil_moisture"]
]

# Target Output
target = dataset["crop_yield"]

 
# Create & Train Model

model = LinearRegression()
model.fit(features, target)

print(" Model training completed") 


# Prediction

print("\n Predicting crop yield...\n") 

sample_input = [[30, 70, 200, 40]]

predicted_yield = model.predict(sample_input)

print(" Predicted Crop Yield:", 
      round(predicted_yield[0], 2),
      "tons/hectare")

print("\n Prediction Successful!")
