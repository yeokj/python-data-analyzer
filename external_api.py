import requests

open_meteo_url = "https://api.open-meteo.com/v1/forecast"

def fetch_hourly_temperature(latitude, longitude, timezone="auto"):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m",
        "forecast_days": 1,
        "timezone": timezone,
    }

    res = requests.get(open_meteo_url, params=params)
    res.raise_for_status()
    data = res.json()

    hourly = data.get('hourly', {})
    times = hourly.get('time', [])
    temperatures = hourly.get('temperature_2m', [])

    return times, temperatures