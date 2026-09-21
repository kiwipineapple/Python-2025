import requests
from pprint import pprint

API_KEY = "ec8798cdc3f558279b9cdda67c12b7fc"
CITY = "guangzhou"
LANG = "zh_cn"

URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang={LANG}"


def get_weather():
    response = requests.get(URL)
    data = response.json()

    print("Response Code:", response.status_code)

    if response.status_code != 200:
        raise RuntimeError(
            data.get("message", "Failed to fetch weather infos"))

    return data

def main():
    data = get_weather()

    city = data['name']

    temp = data['main']['temp']
    print(f'{city}: {temp}')

if __name__ == "__main__":
    main()
