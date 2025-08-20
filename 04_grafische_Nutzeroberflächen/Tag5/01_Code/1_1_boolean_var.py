import tkinter as tk


# Funktion zur Anzeige des aktuellen Werts
# .get() liest den aktuellen Zustand der BooleanVar:
# - True  → Benutzer hat die Checkbox aktiviert
# - False → Benutzer hat die Checkbox deaktiviert
def zeige_status():
    print("Checkbox ausgewählt:", zustand.get())

root = tk.Tk()
root.title("BooleanVar Beispiel mit Checkbutton")

# Was ist eine BooleanVar?
# Eine BooleanVar ist eine spezielle Variable in Tkinter,
# die nur zwei Werte speichern kann: True oder False.
# Sie wird z.B. bei Checkboxen verwendet, um zu merken, ob diese angeklickt wurden oder nicht.
zustand = tk.BooleanVar()
zustand.set(False)  # Anfangswert: nicht ausgewählt


# Checkbutton erstellt, verbunden mit der BooleanVar
check = tk.Checkbutton(root, text="Ich bin einverstanden", variable=zustand, command=zeige_status)

check.pack(padx=20, pady=10)

root.mainloop()
