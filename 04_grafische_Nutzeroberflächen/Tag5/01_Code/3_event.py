import tkinter as tk

# Funktion für Button-Klick (wird über command= ausgelöst)
def on_click():
    print("Button wurde geklickt!")

# Funktion für Tastendruck (wird über bind() ausgelöst)
def on_key(event):
    print(event)
    print("Taste gedrückt:", event.keysym)
# event.char enthält das Zeichen der gedrückten Taste, z.B. "a" oder "B"
# Für Sondertasten wie Shift oder Pfeiltasten ist event.char leer

# Fenster erstellen
root = tk.Tk()
root.title("Eventhandling-Beispiel")
root.geometry("300x150")

# Button erstellen und mit command verbinden
button = tk.Button(root, text="Klick mich", command=on_click)
button.pack(pady=20)

# bind() verbindet ein beliebiges Event mit einer Funktion
# In diesem Fall: jede gedrückte Taste löst on_key() aus
root.bind("<Key>", on_key)

# Haupt-Event-Schleife starten
root.mainloop()
