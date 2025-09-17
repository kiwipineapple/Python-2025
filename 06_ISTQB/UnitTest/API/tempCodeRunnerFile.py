API_KEY = "a40d32d92994f36fbf31e815dc7b86b7"


# URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang={LANG}"


# def get_weather():
#     response = requests.get(URL)
#     data = response.json()

#     print("Response Code:", response.status_code)

#     if response.status_code != 200:
#         raise RuntimeError(
#             data.get("message", "Failed to fetch weather infos"))

# def main():
#     for city in CITYS:
#         get_weather()