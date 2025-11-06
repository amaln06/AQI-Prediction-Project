from datetime import datetime, timedelta
import pandas as pd
from feature_pipeline import fetch_aqi_data

print("🚀 Generating past AQI data for training...")

all_data = []
today = datetime.today()

for i in range(30):
    date = today - timedelta(days=i)
    print(f"📅 Fetching data for: {date.strftime('%Y-%m-%d')}")
    df = fetch_aqi_data(date)
    if not df.empty:
        all_data.append(df)

full_df = pd.concat(all_data, ignore_index=True)
full_df.to_csv("training_data.csv", index=False)
print(f"✅ Saved {len(full_df)} rows (with AQI) to training_data.csv")
