from datetime import datetime as dt, timezone
import requests
import pyfiglet

import colorama
from colorama import Fore

colorama.init(autoreset=True)


with open("my_key.txt", "r") as file:
    api_key = file.read()


def asking_user_city():
    print("Please enter the name of the city you want to check the weather for:")
    return input("City (e.g., Tbilisi): ")


def asking_user_color():
    valid_colors = {"red", "green", "yellow", "blue", "magenta", "cyan", "white"}
    while True:
        print("Choose a color for your weather info:")
        print(f"Available colors: {valid_colors}")
        color = input("Choose a color (e.g., blue): ").lower()
        if color in valid_colors:
            return color
        else:
            print("Invalid color! Please choose a color from the list.")


def color_to_colorama(color):
    return getattr(Fore, color.upper(), Fore.WHITE)


def make_url(city):
    is_complete = False
    while not is_complete:
        try:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=dceb1e36e4625956b5aca3c3b255d39a"
            response = requests.get(url)
            response.raise_for_status()
            is_complete = True
            return response.json(), city
        except:
            print("Wrong City! Try Again...")
            city = asking_user_city()


def kelvin_to_celsius(kelvin):
    return round(kelvin - 273.15)


def all_about_weather(response):
    temp_kelvin = response["main"]["temp"]
    temp_celsius = kelvin_to_celsius(temp_kelvin)
    description = response["weather"][0]["description"]

    timezone_offset = response["timezone"]

    sunrise_time = dt.fromtimestamp(
        response["sys"]["sunrise"] + timezone_offset, tz=timezone.utc
    )
    sunset_time = dt.fromtimestamp(
        response["sys"]["sunset"] + timezone_offset, tz=timezone.utc
    )

    return temp_celsius, description, sunrise_time, sunset_time


def check_description(descrtiption):
    if descrtiption not in weather.keys():
        default_description = "🌫️"
        return default_description
    else:
        return weather[descrtiption]



weather = {
    "clear sky": "☀️",
    "few clouds": "🌤️",
    "scattered clouds": "☁️",
    "broken clouds": "☁️ ☁️",
    "shower rain": "🌧",
    "rain": "🌧️",
    "thunderstorm": "⛈️",
    "snow": "🌨️ ❄️",
    "mist": "🌫️",
    "light rain": "🌧️",
}


def main():
    firstCity = asking_user_city()
    color = asking_user_color()
    user_chosen_color = color_to_colorama(color)
    response, city = make_url(firstCity)
    temp_celsius, description, sunrise_time, sunset_time = all_about_weather(response)
    new_description = check_description(description)
    ascii_text = pyfiglet.figlet_format(f"weather in {city}")

    print(user_chosen_color + ascii_text)

    print(f"🌡️  Current Temperature: {temp_celsius}°C")
    print(f"🌤️  Weather Description: {description} {new_description}")
    print(f"🌅 Sunrise : {sunrise_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🌄 Sunset : {sunset_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("Thank you for using the Weather App! Have a sunny day! 😎🌈")
    
main()
