# Wetterdaten analysieren mit MongoDB (leicht)

## Ziel

Du arbeitest mit einer neuen Collection `weather` und führst verschiedene Analysen mit normalen `find()`-Abfragen durch. 

## Vorbereitung

Lege die Collection `weather` an und füge folgende Einträge ein:

```js
db.weather.insertMany([
  { city: "Berlin", date: "2023-07-01", temperature: 27, humidity: 60, wind: 12, rain: false },
  { city: "Berlin", date: "2023-07-02", temperature: 24, humidity: 65, wind: 18, rain: true },
  { city: "Berlin", date: "2023-07-03", temperature: 22, humidity: 70, wind: 9, rain: false },
  { city: "Paris", date: "2023-07-01", temperature: 30, humidity: 55, wind: 15, rain: false },
  { city: "Paris", date: "2023-07-02", temperature: 28, humidity: 60, wind: 14, rain: true },
  { city: "Paris", date: "2023-07-03", temperature: 26, humidity: 58, wind: 10, rain: false },
  { city: "London", date: "2023-07-01", temperature: 21, humidity: 75, wind: 20, rain: true },
  { city: "London", date: "2023-07-02", temperature: 19, humidity: 80, wind: 22, rain: true },
  { city: "London", date: "2023-07-03", temperature: 18, humidity: 85, wind: 25, rain: true }
])
```

## Aufgaben

1. Finde alle Wetterdaten von Berlin.
2. Finde alle Einträge, bei denen es geregnet hat.
3. Finde alle Tage, an denen die Temperatur unter 20 Grad lag.
4. Finde alle Daten mit Windgeschwindigkeit über 20 km/h.
5. Finde alle trockenen Tage (rain = false) mit mehr als 60 % Luftfeuchtigkeit.
6. Finde alle Tage, an denen es geregnet hat und die Temperatur gleichzeitig über 25 Grad lag.
7. Gib nur die Städte und Temperaturen aus, ohne `_id`.
8. Sortiere alle Daten nach Temperatur absteigend.
9. Finde alle Einträge vom 2. Juli 2023.
10. Welche Städte hatten weniger 60 % Luftfeuchtigkeit?


