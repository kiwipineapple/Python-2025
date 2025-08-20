def nutzerprofil(**infos):
    print(infos)
    #print(infos.items())
    for key, value in infos.items():
        print(f"{key}: {value}")

nutzerprofil(name="Anna", beruf="Lehrerin", ort="Berlin")



"""
def drucke_nachrichten(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


drucke_nachrichten(a="Hallo", b="Welt", c="Meaw!", stadt="Bremen")
# Ausgabe:
# a: Hallo
# b: Welt


"""
