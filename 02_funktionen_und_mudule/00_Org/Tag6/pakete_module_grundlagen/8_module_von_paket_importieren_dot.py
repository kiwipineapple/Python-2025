
"""
Modul:
Ein Modul dient dazu, Python-Code (z.B. Funktionen, Klassen) in einer einzelnen .py-Datei 
zu strukturieren und wiederzuverwenden. Es hilft, den Code übersichtlich und wartbar zu halten.

Paket:
Ein Paket ermöglicht es, mehrere Module in einem Ordner logisch zu gruppieren.
Es wird verwendet, um größere Programme zu organisieren und thematisch zusammengehörende 
Module zu bündeln.

Beispiel: Das Paket email - besteht aus mehreren Modulen wie message, mime.text usw.
Das Paket email ist Teil der Python-Standardbibliothek und dient zum Erstellen, Parsen und Versenden von E-Mails.
"""

"""
->Wir haben einen Paket(Ordner) namens tier,
->in diesem Ordner eine Datei namens katze,
->in dieser Datei eine Funktion namens meaw().
->Wir möchten auf diese Funktion zugreifen.
"""


#import tier.katze
#tier.katze.meaw()


"""
# möglichkeit 1


import tier.hund
tier.hund.bark()
"""


"""
# möglichkeit 2
from tier.katze import meaw
meaw()

from tier.hund import bark
bark()
"""

""""
from tier import katze, hund
katze.meaw()
hund.bark()  
"""

"""
# falls in __init__.py schon geladen 

"""
from tier import meaw,bark
meaw()
bark()



"""
#Diese Syntax bringt ModuleNotFoundError:
import tier.katze.meaw
    
    Wenn Sie per Punktnotation importieren, sollte das letzte Element immer ein Modul sein,
    das die Funktionen enthält.
    Hier ist das letzte Element jedoch kein Modul, sondern eine Funktion innerhalb eines Moduls.
"""


