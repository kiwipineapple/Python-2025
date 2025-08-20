"""

Stell dir vor, du entwickelst eine Anwendung, bei der Nutzer bestimmte Einstellungen vornehmen können
– zum Beispiel Theme, Sprache, Schriftgröße usw.

Nicht alle Einstellungen sind aber immer gesetzt – und manche fehlen vielleicht,
weil der Benutzer sie nicht angepasst hat.

Du sollst eine Klasse Einstellungen erstellen, die es erlaubt, beliebige Konfigurationswerte als
Attribut aufzurufen.
Wenn ein bestimmter Wert nicht vorhanden ist, soll dein Objekt nicht abstürzen,
sondern stattdessen einen Hinweistext zurückgeben – z.B.: "Nicht gesetzt".

z.B
config = Einstellungen()
config.sprache = "Deutsch"

print(config.sprache)     # Erwartet: Deutsch
print(config.theme)       # Erwartet: Nicht gesetzt
print(config.ton)         # Erwartet: Nicht gesetzt
"""
