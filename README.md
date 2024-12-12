# 🌤️ Weather App 🌤️

Welcome to the **Weather App**! This simple and fun Python program helps you check the weather of any city in the world. You can see the current temperature, weather description, and the times for sunrise and sunset – all in a colorful and friendly format!

Whether you're new to programming or just need to quickly check the weather, this app is here to help you! 🚀

## Features 📜

- **City Weather Info**: Get real-time weather information for any city 🌍
- **Colorful Display**: Customize the output with your favorite color 🌈
- **Detailed Info**:
  - Current **Temperature** (in Celsius) 🌡️
  - **Weather Description** (sunny, rainy, cloudy) 🌧️☀️🌨️
  - **Sunrise** and **Sunset** times 🌅🌄
- **Command-Line Interface**: A simple interface with ASCII art for a fun touch 🎨

## Before You Start 🚦

### 1. **Install Python** 🐍
This app is written in Python, so you’ll need Python installed on your computer.

- **How to check if you have Python installed**:  
  Open your terminal or command prompt and type:

  ```bash
  python --version
# Weather App Setup and Usage Guide

## 1. Check if Python is Installed 🐍

Before running the app, make sure Python is installed on your system.

- If Python is installed, you'll see something like `Python 3.x.x` when you run this command in the terminal:

    ```bash
    python --version
    ```

- If it's not installed, you can [download and install Python here](https://www.python.org/downloads/).

---

## 2. Install Required Libraries 📦

The Weather App uses several libraries to fetch and display weather data. To install these dependencies, follow these steps:

1. Open your terminal or command prompt.
2. Run the following command to install the required libraries:

    ```bash
    pip install requests pyfiglet colorama
    ```

This will install:

- `requests` to fetch weather data from the internet 🌍
- `pyfiglet` to display cool ASCII art 🎨
- `colorama` to add colors to your terminal text 🌈

---

## 3. Get Your OpenWeatherMap API Key 🌐

To retrieve weather data, the app uses the OpenWeatherMap API. You’ll need an API key (a secret code) to make requests.

### How to get your API key:

1. Visit [OpenWeatherMap](https://openweathermap.org/).
2. Sign up for a free account.
3. After logging in, go to your account settings and copy your API key.
4. Create a file named `my_key.txt` and paste your API key inside it.

> **Important:** Ensure the `my_key.txt` file is located in the same folder as the Python script.

---

## 4. How to Run the Weather App 🖥️

Follow these steps to run the app:

### Step 1: Download the Weather App

- If you haven’t downloaded the app yet, click the **Code** button above and select **Download ZIP**. 
- Extract the ZIP file into a folder on your computer.

### Step 2: Run the App

1. Open your terminal (or command prompt).
2. Navigate to the folder where you saved the weather app files.
3. Run the app by typing the following command:

    ```bash
    python main.py
    ```

### Step 3: Answer the Questions

- The app will prompt you to enter a city name. For example, you can type `Tbilisi` or `London` and press **Enter**.
- Next, it will ask you to choose a color for the text. You can select from:
  - `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`.
- Type your color choice and hit **Enter**.

---

## 5. Check the Weather! 🌞🌧️❄️

The app will now display the following weather information:

- **Temperature** (in Celsius) 🌡️
- **Weather Description** (e.g., sunny, cloudy, rainy) 🌧️☀️
- **Sunrise and Sunset Times** 🌅🌄

# Example 📝
```bash
Please enter the name of the city you want to check the weather for:
City (e.g., Tbilisi): TBilisi
Choose a color for your weather info:
Available colors: {'yellow', 'red', 'blue', 'green', 'cyan', 'white', 'magenta'}
Choose a color (e.g., blue): blue
                    _   _                 _         _____ ____  _ _ _     _ 
__      _____  __ _| |_| |__   ___ _ __  (_)_ __   |_   _| __ )(_) (_)___(_)
\ \ /\ / / _ \/ _` | __| '_ \ / _ \ '__| | | '_ \    | | |  _ \| | | / __| |
 \ V  V /  __/ (_| | |_| | | |  __/ |    | | | | |   | | | |_) | | | \__ \ |
  \_/\_/ \___|\__,_|\__|_| |_|\___|_|    |_|_| |_|   |_| |____/|_|_|_|___/_|
                                                                            

🌡️  Current Temperature: 6°C
🌤️  Weather Description: clear sky ☀️
🌅 Sunrise : 2024-12-12 08:18:42
🌄 Sunset : 2024-12-12 17:30:28
Thank you for using the Weather App! Have a sunny day! 😎🌈

```
Enjoy your weather forecast! 🌤️
