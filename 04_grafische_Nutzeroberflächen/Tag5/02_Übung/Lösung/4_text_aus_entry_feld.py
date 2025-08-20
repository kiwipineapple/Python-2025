import tkinter as tk

# Funktion, die beim Klick auf den Button ausgeführt wird
def anzeigen():
    print("Eingabe:", eingabe_var.get())  # Gibt den aktuellen Wert der StringVar aus
    # print("Eingabe:", entry.get()) # Wert direkt von Widget

# Hauptfenster erstellen
root = tk.Tk()
root.title("Aufgabe 3: Entry auslesen mit StringVar")

# StringVar zur Verbindung mit dem Entry-Feld
eingabe_var = tk.StringVar()

# Entry-Feld, verbunden mit der StringVar
entry = tk.Entry(root, textvariable=eingabe_var)
entry.pack(pady=5)

# Button, der beim Klicken die Funktion 'anzeigen' aufruft
button = tk.Button(root, text="Anzeigen", command=anzeigen)
button.pack(pady=5)

# GUI starten
root.mainloop()











