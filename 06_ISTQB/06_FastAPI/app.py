# pip install fastapi uvicorn
from fastapi import FastAPI

app = FastAPI()

lat = 45.133
lon = 7.367
API_Key = 'ec8798cdc3f558279b9cdda67c12b7fc'

base_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_Key}"


@app.get(base_url)
def root():
    return {"msg": "welcome"}
