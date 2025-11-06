import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import numpy as np



print("🚀 STEP 3: Starting model training...")

# 1️⃣ Load dataset
df = pd.read_csv("training_data.csv")
print(f"✅ Loaded dataset with {len(df)} rows")

# 2️⃣ Features aur Target define karo
if "aqi" in df.columns:
    y = df["aqi"]
else:
    print("⚠️ 'aqi' column not found! Using temperature as dummy target for now.")
    y = df["temp"]

# Drop non-numeric columns like 'city' or 'date'
X = df.drop(columns=["city", "date", "aqi"], errors="ignore")

# 3️⃣ Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4️⃣ Train Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5️⃣ Predictions
y_pred = model.predict(X_test)

# 6️⃣ Evaluation
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("\n📊 Model Evaluation Results:")
print(f"MAE:  {mae:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R²:   {r2:.2f}")

# 7️⃣ Save trained model
joblib.dump(model, "trained_model.pkl")
print("\n✅ Model saved as trained_model.pkl")

# ✅ MLflow logging
import os
import mlflow
os.makedirs("mlruns", exist_ok=True)
mlflow.set_tracking_uri("file:./mlruns")
mlflow.set_experiment("AQI_Forecast_Models")


# --------------------------------------------------
# 8️⃣ Log model to MLflow (Model Registry)
# --------------------------------------------------
import mlflow
import mlflow.sklearn

mlflow.set_tracking_uri("file:///C:/Users/CW/Desktop/AQI_Prediction_Project/mlruns")
mlflow.set_experiment("AQI_Forecast_Models")

with mlflow.start_run():
    # Log metrics
    mlflow.log_metric("MAE", mae)
    mlflow.log_metric("RMSE", rmse)
    mlflow.log_metric("R2", r2)

    # Log model
    mlflow.sklearn.log_model(model, "model")

print("✅ Model and metrics logged successfully to MLflow Registry!")