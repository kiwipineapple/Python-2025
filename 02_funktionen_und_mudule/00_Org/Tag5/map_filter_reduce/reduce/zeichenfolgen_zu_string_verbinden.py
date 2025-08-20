# Beispiel – Zeichenfolgen zu einem String verbinden

from functools import reduce

texte = ["Python", "macht", "Spaß"]

satz = reduce(lambda x, y: x + " " + y, texte)

print(satz)

"""
reduce() nimmt zwei Strings, fügt sie zusammen, dann das Ergebnis mit dem nächsten, usw.

"Python" + "macht" → "Python macht"

"Python macht" + "Spaß" → "Python macht Spaß"
"""