# 🌤️ Weather Data Collector

This is my first Python project, built as part of my journey to learn Python and practical programming.

The project is a simple weather data collector that uses the **Open-Meteo API** to find a city's geographical coordinates and retrieve its current weather information.

---

## 📌 About the Project

The program works with two main steps:

### 1. Find a City

- The user enters a city name.
- The program sends the city name to the Open-Meteo Geocoding API.
- It receives information about the city, including:
  - Name
  - Latitude
  - Longitude
- The location information is stored in a JSON file.

### 2. Get Weather Data

- The user selects a city.
- The program reads the city's latitude and longitude from the JSON file.
- These coordinates are sent to the Open-Meteo Weather API.
- The program retrieves current weather information such as:
  - Temperature
  - Relative humidity
  - Wind speed
- The weather information is stored in another JSON file.

---

## ⚙️ How It Works

The general workflow of the project is:

```text
User enters a city
        ↓
Geocoding API
        ↓
City name + Latitude + Longitude
        ↓
Save location data in JSON
        ↓
User selects a city
        ↓
Read coordinates from JSON
        ↓
Weather API
        ↓
Temperature + Humidity + Wind Speed
        ↓
Save weather data in JSON
