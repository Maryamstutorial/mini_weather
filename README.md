# 🌤️ Weather App

This is a beginner-friendly **Python Weather App** that uses the **Open-Meteo API** to get weather information.

## 📌 What This Project Does

The program works in two steps:

### 1️⃣ Islamabad Weather

First, the program gets weather information for **Islamabad** using its fixed latitude and longitude.

It displays:

* 🌡️ Temperature
* 💧 Humidity
* ☁️ Weather code
* 💨 Wind speed

### 2️⃣ User's City Weather

After displaying Islamabad's weather, the program asks the user to enter a city name.

For example:

```text
Enter your city: Lahore
```

The program then:

* Finds the city's latitude and longitude.
* Uses those coordinates to get weather information.
* Displays the weather for the city entered by the user.

## 🛠️ Technologies Used

* Python 🐍
* `requests` library
* Open-Meteo API
* JSON
* Dictionaries
* User input

## 📚 What I Learned

While making this project, I learned:

* How to install and import the `requests` library.
* How to send a GET request using `requests.get()`.
* What an API is.
* How to work with API URLs.
* How `.json()` converts API data into a Python dictionary.
* How to access data from nested dictionaries.
* How to take user input using `input()`.
* How to use latitude and longitude.
* How to create dynamic API URLs using f-strings.

## 🔧 Installation

Install the `requests` library:

```bash
pip install requests
```

Then run the Python file:

```bash
python weathe.py
```

## 💻 Example

```text
This is the current weather status {...}
This is weather temperature 30.5
This is weather humidity 45
This is weather code 2
This is wind speed 12.3

Enter your city: Lahore

City: Lahore
Temperature: 31.2 °C
Humidity: 50 %
Weather code: 1
Wind speed: 10.5 km/h
```

## 🚀 Future Improvements

In the future, I would like to:

* Add weather descriptions instead of only weather codes.
* Add error handling for invalid city names.
* Add a 7-day weather forecast.
* Add more weather information.
* Create a simple GUI for the application.

## 👩‍💻 Project Level

**Beginner Python Project**

This project helped me practice **Python, APIs, JSON, dictionaries, user input, f-strings, and the `requests` library**.
