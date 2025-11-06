import pandas as pd
import joblib

print("🔮 STEP 2: Predicting next 3 days AQI...")

# Load trained model
model = joblib.load("trained_model.pkl")

# Load forecast data
forecast_df = pd.read_csv("forecast_data.csv")

# Select only numerical columns used for training
X_forecast = forecast_df[["temp", "humidity", "pressure", "wind_speed"]]

# Predict AQI using trained model
forecast_df["predicted_aqi"] = model.predict(X_forecast)

# Save predictions
forecast_df.to_csv("forecast_with_aqi.csv", index=False)

print("✅ Predictions saved in forecast_with_aqi.csv")
print("\n📈 Sample predictions:")
print(forecast_df[["date_time", "predicted_aqi"]].head(10))
