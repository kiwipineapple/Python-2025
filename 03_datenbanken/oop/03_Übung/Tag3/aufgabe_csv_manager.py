"""(MITTEL)

THEMA: OOP
Benötigtes Wissen: csv-Modul, pathlib

Erstelle eine Klasse CSV-Manager, die eine CSV-Datei einliest.
Die ausgegeben Felder sollen über eine Property columns gesetzt werden können.

Erstelle dazu eine CSV-Datei oder nutze die beiliegende Datei `data.csv`.
Die read-Methode soll ein Generator sein, der die Zeilen der CSV-Datei zurückgibt (yield).
falls yield noch nicht bekannt ist, kann read() auch eine Liste zurückgeben.

1) Beispiel (mit read als Generator):
manager = CsvManager(filename="data.csv")
manager.columns = ["id", "age", "height"]
print(list(manager.read()))

{'id': '23', 'age': '4', 'height': '2'}
{'id': '223', 'age': '14', 'height': '22'}
{'id': '123', 'age': '4', 'height': '3422'}

2) Beispiel (mit read als Liste):
manager = CsvManager(filename="data.csv")
manager.columns = ["id", "age", "height"]
print(manager.read())

[
    {'id': '23', 'age': '4', 'height': '2'}
    {'id': '223', 'age': '14', 'height': '22'}
    {'id': '123', 'age': '4', 'height': '3422'}
]

"""

from pathlib import Path
import csv
