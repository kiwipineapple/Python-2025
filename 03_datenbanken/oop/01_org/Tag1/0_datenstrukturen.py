# Datenstrukturen

# Fixpunkt im kart. Koordinatensystem
fix_point = (1.0, 2.3)  # unveränderlich

# Messreihe
messreihe = [2, 23, 2]

# komplexere Datenstruktur
data_entry = {
    "name": "Sensor1",
    "position": (3, 3),
    "values": [2, 3, 4],
}


def generate_entry(name: str, x: float, y: float, values: list) -> dict:
    """Create Data Entry Dict."""
    data_entry = {
        "name": name,
        "position": (x, y),
        "values": values,
    }
    return data_entry


data = [
    ("Sensor1", 1, 3, [2, 3, 4, 5]),
    ("Sensor2", 12, 3, [2, 3, 4, 5]),
    ("Sensor3", 1, 3, [2, 3, 4, 5]),
]


# Erstelle Data Entry "Objekte" und speichere sie in data_entries
data_entries = []
for name, x, y, values in data:
    data_entries.append(generate_entry(name, x, y, values))

print(data_entries[0]["name"])
