# 🌤️ Weather Data Fetcher

A real-time weather tool that fetches live atmospheric data from any city in the world using the **OpenWeatherMap API**.

## 🚀 Features
* **Live Updates:** Fetches current temperature and weather conditions (e.g., "clear sky", "light rain").
* **Error Handling:** Gracefully handles invalid city names to prevent crashes.
* **Unit Conversion:** Displays temperature in Celsius using the Metric system.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Library:** `requests` (for API calls)
* **Data Format:** JSON
* **API:** [OpenWeatherMap](https://openweathermap.org/api)

## 📖 How to Run
1. Ensure you have the `requests` library installed: `pip install requests`
2. Run the script: `python weather_fetcher.py`
3. Enter any city name when prompted.

## 🔑 Setup & API Key
This project requires a free API key from [OpenWeatherMap](https://openweathermap.org/api). 
1. Sign up and generate a "Current Weather Data" API key.
2. Open `weather_fetcher.py`.
3. Replace `YOUR_API_KEY_HERE` with your actual key.
