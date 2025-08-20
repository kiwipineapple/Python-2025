print("Das Modul 'wetter' wurde importiert – bereit für Temperaturanalysen!")

a = 5
if a < 0:
    print("Eiskalt")
elif a < 10:
    print("kalt")
else:
    print("Meaw")


def beschreibung(temp):

    print("hallo meaw") # aufgabe 1

    #aufgabe 2
    if temp < 0:
        return "Eiskalt"
    elif temp < 10:
        return "Kalt"
    elif temp < 20:
        print("geklappt")
        # return "Mild"
    elif temp < 30:
        return "Warm"
    else:
        return "Heiß"

    # aufgabe 3

    # aufgabe 4
