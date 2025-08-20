import tkinter as tk

# Diese Funktion wird aufgerufen, wenn die Leertaste gedrückt wird
def farbe_wechseln(event):
    # Der Hintergrund des Fensters wird geändert
    root.config(bg="lightblue")

# Hauptfenster erstellen
root = tk.Tk()
root.title("Aufgabe 4: bind() und Leertaste")
root.geometry("300x150")

# Leertaste mit Funktion verbinden
root.bind("<space>", farbe_wechseln)

# Info-Label anzeigen
# tk.Label(root, text="Drücke die Leertaste").pack(pady=30)
label = tk.Label(root, text="Drücke die Leertaste")  # Schritt 1: Label erstellen
label.pack(pady=30)                                  # Schritt 2: im Fenster platzieren


# GUI starten
root.mainloop()
