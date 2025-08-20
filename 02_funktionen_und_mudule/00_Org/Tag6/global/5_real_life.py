balance = 1000  # Globale Variable für den Kontostand

def deposit(amount):
    global balance  # Wir erklären, dass wir die globale Variable balance verwenden wollen
    balance += amount
    print(f"{amount} EUR eingezahlt. Neuer Kontostand: {balance} EUR.")

def withdraw(amount):
    global balance  # Globale Variable verwenden, um den neuen Kontostand zu speichern
    if amount <= balance:
        balance -= amount
        print(f"{amount} EUR abgehoben. Neuer Kontostand: {balance} EUR.")
    else:
        print(f"Abhebung fehlgeschlagen. Nicht genug Guthaben. Aktueller Kontostand: {balance} EUR.")

# Testfälle
deposit(200)
withdraw(500)
withdraw(800)
deposit(500)


"""
Ein Beispiel für die reale Anwendung des global-Schlüsselworts könnte ein einfaches Banking-System sein, 
in dem wir den Kontostand einer Person verwalten. 

Stellen wir uns vor, wir haben eine globale Variable, die den aktuellen Kontostand speichert, 
und wir möchten Funktionen implementieren, die Einzahlungen und Abhebungen ermöglichen.

"""