import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import mlflow

# ============================================================
# STEP 1: Load Dataset
# ============================================================
print("🚀 STEP 1: Loading dataset...")
data_path = "data/aqi_data.csv"

if not os.path.exists(data_path):
    raise FileNotFoundError(f"❌ Dataset not found at {data_path}")

df = pd.read_csv(data_path)
print(f"✅ Loaded dataset with {len(df)} rows\n")

# ============================================================
# STEP 2: Prepare Data
# ============================================================
print("⚙️ STEP 2: Preparing data...")
X = df.drop("AQI", axis=1)
y = df["AQI"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("✅ Data split done\n")

# ============================================================
# STEP 3: Train Model
# ============================================================
print("🏋️ STEP 3: Training model...")
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)
r2 = r2_score(y_test, y_pred)

print("\n📊 Model Evaluation Results:")
print(f"MAE:  {mae:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R²:   {r2:.2f}\n")

# ============================================================
# STEP 4: Save Trained Model
# ============================================================
model_path = "trained_model.pkl"
joblib.dump(model, model_path)
print(f"✅ Model saved as {model_path}\n")

# ============================================================
# STEP 5: MLflow Experiment Tracking (Safe for GitHub Actions)
# ============================================================
print("📦 STEP 5: Logging to MLflow...")

# Safe universal MLflow directory
tracking_dir = os.path.join(os.getcwd(), "mlruns")
os.makedirs(tracking_dir, exist_ok=True)

# Set MLflow to use local folder instead of Windows drive
mlflow.set_tracking_uri(f"file://{tracking_dir}")
mlflow.set_experiment("AQI_Forecast_Models")

with mlflow.start_run():
    mlflow.log_param("model_type", "LinearRegression")
    mlflow.log_metric("MAE", mae)
    mlflow.log_metric("RMSE", rmse)
    mlflow.log_metric("R2", r2)
    mlflow.log_artifact(model_path)

print("✅ MLflow logging completed successfully!\n")
print("🎯 Training pipeline finished successfully!")