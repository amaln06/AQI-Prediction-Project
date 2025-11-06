import pandas as pd
import streamlit as st

# Load prediction data
df = pd.read_csv("forecast_with_aqi.csv")

st.title("🌍 3-Day AQI Forecast Dashboard")
st.write("City: **Karachi**")

st.line_chart(df.set_index("date_time")["predicted_aqi"])

st.dataframe(df[["date_time", "temp", "humidity", "pressure", "wind_speed", "predicted_aqi"]])
