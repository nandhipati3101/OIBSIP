import requests

api = "af65cc8c73716b9270d9cfbc2e77ce00"
city = input("Enter the city: ")

weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api}")

if weather.status_code == 404:
    print("Invalid city name")
else:
    weather_data = weather.json()["weather"][0]["main"]
    temp=weather.json()["main"]["temp"]
    hum=weather.json()["main"]["humidity"]
    print(f"the weather in {city} is {weather_data} and temperature is {temp} F")
    print(f"the humidity in the region is :{hum}")
    