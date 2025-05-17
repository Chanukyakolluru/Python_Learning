import requests
import json

API_KEY = "fa3703e8b03efd23e5bb38a95ad5c538"  # Replace with your actual API key
CITY = ("Hyderabad")
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def weather():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        pretty_json = json.dumps(data, indent=4)
        print(pretty_json)
        print(f"Weather in {CITY}: {data['weather'][0]['description']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity:{data['main']['humidity']}°C")
    else:
        print(f"Error: {response.status_code} - {response.text}")

weather()