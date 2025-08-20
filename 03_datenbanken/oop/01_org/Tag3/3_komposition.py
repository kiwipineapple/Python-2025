"""
Komposition ist eine Assoziation und definiert durch
eine Teil-Ganzes-Beziehung. Das Teil existiert NICHT weiter, wenn das
Ganze gelöscht wird.

Ein Gebäude hat Zimmer (und ein Zimmer kann ohne Gebäude nicht existieren).


classDiagram
    class Room {
        name: String
    }

    class Building {
        addresse: String
        rooms: List~Room~
    }

    Building *-- Room : contains
"""


class Room:
    def __init__(self, name):
        self.name = name


class Building:
    def __init__(self, name, rooms: list[Room]):
        self.name = name
        self.rooms = rooms


baker_street = Building(
    "Baker Street 221b",
    rooms=[
        Room("Kitchen"),
        Room("Living Room"),
    ],
)

baker_street.rooms.append(Room("Basement"))
del baker_street
