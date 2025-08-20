import tkinter as tk

# Funktion, die beim Klick auf einen Radiobutton ausgeführt wird
def auswahl_anzeigen():
    print("Ausgewählt:", auswahl.get())  # Gibt den aktuell ausgewählten Wert aus

# Hauptfenster erstellen
root = tk.Tk()
root.title("Radiobuttons ohne Vorauswahl")

# StringVar für die Auswahl definieren
# Startwert ist "unselected", dieser passt zu keinem Radiobutton → also bleibt alles abgewählt
auswahl = tk.StringVar(value="unselected")

# Radiobutton 1 mit Wert "Männlich"
rb1 = tk.Radiobutton(root, text="Männlich", variable=auswahl, value="Männlich", command=auswahl_anzeigen)

# Radiobutton 2 mit Wert "Weiblich"
rb2 = tk.Radiobutton(root, text="Weiblich", variable=auswahl, value="Weiblich", command=auswahl_anzeigen)

# Radiobuttons im Fenster platzieren
rb1.pack()
rb2.pack()

# Haupt-Event-Schleife starten (GUI anzeigen)
root.mainloop()
