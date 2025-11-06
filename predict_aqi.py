import joblib
import pandas as pd
from feature_pipeline import fetch_aqi_data

print("🔮 Loading model and predicting AQI...")

# Load trained model
model = joblib.load("trained_model.pkl")

# Fetch latest data using API
df = fetch_aqi_data()
print("\n🌤️ Current data fetched:")
print(df)

# Select features for prediction
X = df[["temp", "humidity", "pressure", "wind_speed"]]

# (No scaler used in training, so skip scaling)
X_scaled = X

# Predict AQI
predicted_aqi = model.predict(X_scaled)[0]

print(f"\n🌍 Predicted AQI for {df['city'][0]} on {df['date'][0]}: {predicted_aqi:.2f}")
