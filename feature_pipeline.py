import requests
import pandas as pd

# ---- CONFIG ----
API_KEY = "004fcb55480a4e1092d4db79a2c7930d"
CITY = "Karachi"

# Get coordinates for AQI API
def get_city_coordinates(city):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()[0]
    return data["lat"], data["lon"]

# Fetch weather + AQI data for given date
def fetch_aqi_data(date=None):
    lat, lon = get_city_coordinates(CITY)
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    aqi_url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"

    weather_res = requests.get(weather_url)
    aqi_res = requests.get(aqi_url)

    if weather_res.status_code == 200 and aqi_res.status_code == 200:
        weather_data = weather_res.json()
        aqi_data = aqi_res.json()

        aqi = aqi_data["list"][0]["main"]["aqi"]  # AQI value from API

        features = {
            "city": CITY,
            "temp": weather_data["main"]["temp"],
            "humidity": weather_data["main"]["humidity"],
            "pressure": weather_data["main"]["pressure"],
            "wind_speed": weather_data["wind"]["speed"],
            "aqi": aqi,
            "date": pd.Timestamp.now().strftime("%Y-%m-%d")
        }

        return pd.DataFrame([features])
    else:
        print("❌ Error fetching data")
        return pd.DataFrame()
