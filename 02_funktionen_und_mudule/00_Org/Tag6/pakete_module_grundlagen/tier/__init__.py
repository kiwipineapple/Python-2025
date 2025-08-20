print("Ich (__init__.py) werde als Erstes ausgeführt")

# Die Datei __init__.py kennzeichnet den Ordner als ein Python-Paket.
# Sie wird automatisch ausgeführt, wenn das Paket importiert wird.
# Man kann sie verwenden, um Startwerte zu setzen oder Initialisierungen vorzunehmen.
from .hund import bark
from .katze import meaw