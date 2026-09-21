import requests
from pprint import pprint

API_KEY = "ec8798cdc3f558279b9cdda67c12b7fc"
CITY = "guangzhou"
LANG = "zh_cn"

URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang={LANG}"

response = requests.get(URL)

data = response.json()

pprint(data)

print(data['name'])
