def zeilen_zaehlen(pfad):
    with open(pfad,'r', encoding='utf-8') as f:
        zeilen = f.readlines()
    return len(zeilen)

def  woerter_zaehlen(pfad):
    with open(pfad,'r', encoding='utf-8') as f:
        inhalt = f.read()
    return len(inhalt.split())