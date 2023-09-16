import requests
import json

def get_weather(api_key, city):
    web_url = "http://api.openweathermap.org/data/2.5/weather?"
    api_created_url = f"{web_url}q={city}&appid={api_key}"

    response = requests.get(api_created_url)
    data = response.json()

    if data["cod"] != "404":
        main_data = data["main"]
        weather_data = data["weather"][0]

        temperature = main_data["temp"]
        pressure = main_data["pressure"]
        humidity = main_data["humidity"]
        description = weather_data["description"]

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature} K")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")
    else:
        print("City is not found.")

def main():
    with open("cities.json") as f:
        data = json.load(f)
        cities = data["cities"]

    api_key = "6dee1cebfab04c0f01810073f2ac480a"  # Replace with your OpenWeatherMap API key

    print("Cities:")
    for city in cities:
        print(city)

    while True:
        entered_city = input("Enter the name of city: ").capitalize()
        if entered_city in cities:
            get_weather(api_key, entered_city)
            break
        else:
            print("City not found in list. Please try again.")

if __name__ == "__main__":
    main()
