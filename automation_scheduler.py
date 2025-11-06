import schedule
import time
import os

def run_feature_pipeline():
    print("⏰ Running feature pipeline...")
    os.system("python fetch_forecast.py")

def run_training_pipeline():
    print("🎯 Running training pipeline...")
    os.system("python train_model.py")

# Har ghante feature update
schedule.every(1).hours.do(run_feature_pipeline)

# Har din training update
schedule.every().day.at("00:00").do(run_training_pipeline)

print("🚀 Automation scheduler started... (Press CTRL+C to stop)")

while True:
    schedule.run_pending()
    time.sleep(60)
