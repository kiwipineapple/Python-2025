import tkinter as tk

# Diese Funktion wird aufgerufen, wenn sich der Inhalt der Entry-Variable ändert
def on_change(*args):
    print("Eingabe geändert:", entry_var.get())

# Hauptfenster erstellen
root = tk.Tk()
root.title("Aufgabe 1: Entry mit trace")

# StringVar definieren und mit trace überwachen
entry_var = tk.StringVar()
entry_var.trace("w", on_change)  # "w" steht für "write" – wird bei Änderungen ausgelöst

# Entry-Feld mit der Variablen verbinden
entry = tk.Entry(root, textvariable=entry_var)
entry.pack(padx=10, pady=10)

# GUI starten
root.mainloop()
