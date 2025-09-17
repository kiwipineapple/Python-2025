import requests
from pprint import pprint
import json

with open('config.json', 'r') as file:
    infos = json.load(file)
    print(infos)


API_KEY = "ec8798cdc3f558279b9cdda67c12b7fc"


def get_weather(city, LANG):
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang={LANG}"
    response = requests.get(URL)
    data = response.json()

    # print("Response Code:", response.status_code)

    if response.status_code != 200:
        raise RuntimeError(
            data.get("message", "Failed to fetch weather infos"))

    return data


def main():
    for city in infos["CITYS"]:
        LANG = infos["LANG"]
        data = get_weather(city, LANG)

        # Temperature
        temp = data["main"]["temp"]

        # Description
        desc = data["weather"][0]["description"]

        print(f"City: {city} - Temp: {temp} - Desc: {desc}")


if __name__ == "__main__":
    main()
