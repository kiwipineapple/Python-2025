"""
**Aufgabe (SCHWER)**

THEMA: OOP, Assoziationen, Aggregation, Komposition

Es sollen Klassen für eine Telefonbuch-App modelliert werden.
Wir benötigen zwei Klassen:

* `Entry`: ein Telefonbuch-Eintrag (mit Name und Telefonnummer)
* `TelephoneBook`: das Telefonbuch, welches Telefonbuch-Einträge verwaltet.

Wichtig:

* Ein `Entry` wird unabhängig vom `TelephoneBook` erstellt und anschließend hinzugefügt.
* Die Telefonnummern müssen Integer sein, das ist die einzige Anforderung.

Beispiel:

```python
book = TelephoneBook(name="privates Telefonbuch")

entry1 = Entry(name="Bob", number="23423432")
book.add(entry1)

entry2 = Entry(name="Alice", number="23423432999")
book.add(entry2)

entry3 = Entry(name="Bob", number="11123423432")
book.add(entry3)
# ValueError("Der Name befindet sich schon im Buch")


entry4 = Entry(name="Trudy", number="AAA23423432")
book.add(entry4)
# ValueError("Die Telefonnummer muss numerisch sein!")

book.list_entries()
# Bob: 232242424
# Alice: 232423211

book.list_entries(filter_name="B")
# Bob: 232242424

book.delete(name="Bob")
# Nutzer Bob wurde gelöscht

book.delete(name="Bob")
# ValueError(konnte kein Nutzer Bob gefunden werden)
```

**Zusatz-Frage:**
Handelt es sich bei der Beziehung zwischen `TelephoneBook` und `Entry` um eine Aggregation oder um eine Komposition? Begründe deine Antwort.
"""
