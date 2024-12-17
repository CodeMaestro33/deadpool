import requests
import json
from datetime import datetime
import os

# Constants
API_KEY = "7d01f2fe488a7b6b0cb360d0d5227ca6"  # Replace with your OpenWeatherMap API key
CITIES = {
    "Berlin": "Berlin,DE",
    "London": "London,GB",
    "India": "Delhi,IN",  # Assuming New Delhi for India
    "Japan": "Tokyo,JP"
}
OUTPUT_FILE = "weather_data.json"

# Function to fetch weather data for a given city
def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching weather for {city}: {response.status_code}")
        return None

# Save the weather data to a JSON file
def save_weather_data():
    weather_info = {}
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for city_name, city_query in CITIES.items():
        data = get_weather_data(city_query)
        if data:
            weather_info[city_name] = {
                "temperature": data["main"]["temp"],
                "weather": data["weather"][0]["description"],
                "time": now
            }

    # Write data to a file
    with open(OUTPUT_FILE, "w") as file:
        json.dump(weather_info, file, indent=4)
    print("Weather data saved.")

# Commit and push the changes to GitHub
def git_commit_push():
    os.system("git add weather_data.json")
    os.system('git commit -m "Updated weather data"')
    os.system("git push origin main")  # Replace 'main' with your branch name if needed

if __name__ == "__main__":
    save_weather_data()
    git_commit_push()
