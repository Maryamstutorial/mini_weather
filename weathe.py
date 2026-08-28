#  Install the requests library ( pip install requests). It allows our program to communicate with websites and APIs 
# API is a messenger between your program and another service.
import requests
# Go to this API and GET/ask for its information."
# API URL tells Python where to get the data from
response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=33.6844&longitude=73.0479&hourly=temperature_2m&current=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m")
# .json() converts the API response into a Python dictionary
# print(response.json())
data=response.json()
print(data)
print("This is the current weather status",data["current"])
print("This is weather temperature",data["current"]["temperature_2m"])
print("This is weather humidity",data["current"]["relative_humidity_2m"])
# 0 → Clear sky
# 1, 2, 3 → Cloudy conditions
# 45, 48 → Foggy
# 51, 53, 55 → Drizzle
# 61, 63, 65 → Rain
print("This is weather code",data["current"]["weather_code"])
print("This is wind speed",data["current"]["wind_speed_10m"])

# now we ask the user for specific city weather
city = input("Enter your city: ")
geo_response = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1")
geo_data = geo_response.json()
print(geo_data)
# Get latitude and longitude
latitude = geo_data["results"][0]["latitude"]
longitude = geo_data["results"][0]["longitude"]
# Get weather information using the city's coordinates
response = requests.get(
    f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m"
)
# Convert weather response into a dictionary
data = response.json()
# Display weather information
print("City:", city)
print("Temperature:", data["current"]["temperature_2m"], "°C")
print("Humidity:", data["current"]["relative_humidity_2m"], "%")
print("Weather code:", data["current"]["weather_code"])
print("Wind speed:", data["current"]["wind_speed_10m"], "km/h")
