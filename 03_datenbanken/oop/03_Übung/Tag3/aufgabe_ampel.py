"""
THEMA: ENUM

Die Ampel kann vier verschiedene Zustände einnehmen:
rot,
rot-gelb,
grün und
gelb.


Definiere einen StrEnum TrafficLightState, der die Zustände einer
Ampel repräsentiert: ROT, ROT-GELB, GRÜN und GELB.

Erstelle eine TrafficLight-Klasse, deren Anfangszustand ROT ist.

Die next_state-Methode simuliert den Übergang von einem
Zustand zum nächsten in der Reihenfolge ROT → ROT-GELB → GRÜN → GELB → ROT...

Simulieren die Zustandsübergänge durch wiederholte Aufrufe von next_state().

traffic_light = TrafficLight()
print("Initial state:", traffic_light) # ROT
traffic_light.next_state()
print("Current state:", traffic_light) # ROT-GELB

for _ in range(5):
    traffic_light.next_state()
    print("Next state:", traffic_light)

Next state: grün
Next state: gelb
Next state: rot
Next state: rot gelb

"""
