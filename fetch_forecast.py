import requests
import pandas as pd
from datetime import datetime

API_KEY = "004fcb55480a4e1092d4db79a2c7930d"
CITY = "Karachi"

def get_city_coordinates(city):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()[0]
    return data["lat"], data["lon"]

def fetch_forecast(city):
    lat, lon = get_city_coordinates(city)
    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    res = requests.get(url)
    data = res.json()

    records = []
    for item in data["list"]:
        date = datetime.fromtimestamp(item["dt"]).strftime("%Y-%m-%d %H:%M:%S")
        temp = item["main"]["temp"]
        humidity = item["main"]["humidity"]
        pressure = item["main"]["pressure"]
        wind_speed = item["wind"]["speed"]
        records.append({
            "city": city,
            "date_time": date,
            "temp": temp,
            "humidity": humidity,
            "pressure": pressure,
            "wind_speed": wind_speed
        })

    df = pd.DataFrame(records)
    df.to_csv("forecast_data.csv", index=False)
    print("✅ Saved 3-day forecast to forecast_data.csv")

if __name__ == "__main__":
    fetch_forecast(CITY)
