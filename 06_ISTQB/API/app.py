import requests
from pprint import pprint

API_KEY = "a40d32d92994f36fbf31e815dc7b86b7"
CITY = "guangzhou"
LANG = "zh_cn"

URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang={LANG}"

response = requests.get(URL)

data = response.json()

pprint(data)
