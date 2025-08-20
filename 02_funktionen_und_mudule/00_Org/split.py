# Thema: split()-Funktion in Python
# Was ist das?
# Die split()-Funktion ist eine Methode für Strings, die einen Text in mehrere Teile zerlegt
# und diese Teile als Liste zurückgibt.

# Standardmäßig wird dabei nach Leerzeichen getrennt.
# Man kann aber auch ein eigenes Trennzeichen angeben, z.B. Komma oder Semikolon.

# Beispiel 1: Standardverhalten – Trennung nach Leerzeichen
text = "Python ist eine tolle Programmier sprache"
woerter_liste = text.split()  # Teilt den Satz in einzelne Wörter
print("Liste der Wörter:", woerter_liste)



# Beispiel 2: Trennung nach einem bestimmten Zeichen
text2 = "Apfel,B   a   n   a  ne,Or   a   nge,M  a   ngo"
fruechte_liste = text2.split("a")  # Trennung nach Komma
print("Liste der Früchte:", fruechte_liste)




# Beispiel 3: split() zusammen mit input()
eingabe = input("Gib ein paar Wörter ein, getrennt durch Leerzeichen: ")
teile = eingabe.split()
print("Du hast folgende Wörter eingegeben:", teile)




# Beispiel 4: Verwendung des Parameters maxsplit
# maxsplit gibt an, wie oft maximal gesplittet werden soll (von links nach rechts)
text3 = "Name:Max Alter:24 Stadt:Berlin"
teile_mit_limit = text3.split(" ", maxsplit=1)  # Nur 1x trennen beim ersten Leerzeichen
print("Mit maxsplit=1:", teile_mit_limit)


# Trennung anhand eines bestimmten Buchstabens
# Wir haben einen künstlichen String, bei dem das Zeichen "x" als Trenner verwendet wurde
text = "Apfel x Banane x Orange x Mango"

# Wir wollen den String an jedem "x" trennen
teile = text.split("x")

print("Liste der Früchte:", teile)
