
"""
Wie sucht Python nach einem Modul beim import?
Wenn du in Python z.B. schreibst:

import mathe_tools

... dann fragt sich Python: „Wo finde ich die Datei mathe_tools.py?“

Dabei geht Python schrittweise durch folgende Orte – in dieser Reihenfolge:

1. Aktuelles Verzeichnis (das Verzeichnis, in dem dein Skript liegt)
Python prüft zuerst, ob im gleichen Ordner wie dein aktuelles Skript eine Datei mathe_tools.py liegt.

Vorteil: Du kannst eigene Module einfach im Projektordner speichern und direkt verwenden.

Ein Modul kann auch dann importiert werden, wenn es sich in einem anderen Verzeichnis befindet –
vorausgesetzt, dieses Verzeichnis wurde dem sys.path hinzugefügt.

import sys
sys.path.append("C:/mein_pfad")

import mein_modul  # funktioniert ohne Pfadangabe


2. Python-Standardbibliothek
Wenn das Modul nicht im aktuellen Ordner ist, prüft Python, ob es Teil der Standardbibliothek ist – also z.B.
sowas wie: math, random, os, datetime

Diese sind fix mit Python installiert, aber nicht automatisch sichtbar im Projektordner.

Python verwendet intern eine Liste von Verzeichnissen, um nach Modulen zu suchen.
Diese Liste kannst du anzeigen mit:
"""
import sys
print(sys.path)

"""


3. site-packages (installierte Module - mit pip)
Falls das Modul auch nicht in der Standardbibliothek ist, schaut Python in den Ordner site-packages,
in dem alle mit pip installierten Pakete liegen:

Beispiele:numpy, pandas, requests

Du findest den Pfad zu site-packages z.B. unter:

"""

import site
print(site.getsitepackages())
