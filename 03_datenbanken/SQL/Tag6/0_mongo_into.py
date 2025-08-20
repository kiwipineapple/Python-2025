"""
MongoDB in python

pip install pymongo
"""

import pymongo
from pymongo.collection import Collection


def update_points(collection: Collection, search: dict, points: int):
    """Diese Funktion soll das Attribut points auf points setzen."""
    collection.update_many(search, {"$set": {"points": points}})


def insert_heroes(collection: Collection, daten: list) -> list:
    """Einige Helden eintragen."""
    result = collection.insert_many(daten)
    return result.inserted_ids


with pymongo.MongoClient("mongodb://localhost:27017/") as client:
    # gibt uns Zugriff auf die Datenbank
    db = client["heroDB"]

    # Zugriff auf die Sammlung heroes
    heroes = db["heroes"]

    helden = [
        {"name": "Thor", "city": "Asgard"},
        {"name": "Loki", "city": "Asgard"},
        {"name": "Hulk", "city": "New York"},
    ]
    eingetragene_helden = insert_heroes(heroes, daten=helden)
    print("Diese ID wurden eingetragen: ", eingetragene_helden)

    update = update_points(heroes, search={"name": "Superman"}, points=100)

    # Alle Heroes finden (erzeugt Cursor Objekt)
    # alle_heroes = heroes.find()

    # alle heroes ausgeben
    # for hero in alle_heroes:
    #     print("=>", hero)

    if not heroes.find_one({"name": "Jocker2"}):
        daten = {"name": "Joker2", "city": "New York"}
        result = heroes.insert_one(daten)
        print("Zuletzt eingefügte ID:", result.inserted_id)

    # db.heroes.find({inventory: {$exists: true}})
    heroes_mit_inventory = heroes.find({"inventory": {"$exists": "true"}})
    for hero in heroes_mit_inventory:
        print("===>", hero)
