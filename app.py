from flask import Flask, render_template, request, jsonify
import re
from external_api import fetch_hourly_temperature
from analyzer import analyze_numbers
from weather_analysis import analyze_temperatures

app = Flask(__name__)


@app.route('/')
def index():
    your_name = "Kyame Israel"
    return render_template('index.html', name=your_name)

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    # Only handle POST form submissions here; GET shows the index page
    if request.method == 'POST':
        request_data = request.form.get('numbers', '')
        # split on commas, whitespace, or newlines and remove empty tokens
        tokens = [t for t in re.split(r'[,\s]+', request_data.strip()) if t]
        if not tokens:
            return render_template('index.html', error='Please enter one or more numbers.')

        try:
            numbers = [float(t) for t in tokens]
        except ValueError:
            return render_template('index.html', error='Invalid input — please enter only numbers (e.g. 1, 2.5, 3).')

        results = analyze_numbers(numbers)
        # render the dedicated results template; match the variable names used by the template
        return render_template('results.html', numbers_list=numbers, analysis=results)

    # GET -> show the form
    return render_template('index.html')

@app.route('/analyze-weather', methods=['GET', 'POST'])
def analyze_weather():
    # Simple handler: use provided lat/lon (POST) or defaults (GET).
    if request.method == 'POST':
        try:
            latitude = float(request.form.get('lat'))
            longitude = float(request.form.get('lon'))
        except (TypeError, ValueError):
            return render_template('weather_input.html', error='Please enter valid numeric latitude and longitude.')
    else:
        latitude = 40.7128
        longitude = -74.0060

    try:
        times, temperatures = fetch_hourly_temperature(latitude, longitude)
        stats = analyze_temperatures(times, temperatures)
        return render_template('weather_analysis_results.html', times=times, temperatures=temperatures, stats=stats)
    except Exception:
        # Keep it simple: show a generic error in the template on failure
        return render_template('weather_analysis_results.html', error='Failed to fetch or analyze weather data.')

@app.route('/weather-input')
def weather_input():
    return render_template('weather_input.html')

if __name__ == "__main__":
    app.run(debug=True)