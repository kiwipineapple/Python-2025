import tkinter as tk

# Diese Funktion wird aufgerufen, wenn ein Radiobutton ausgewählt wird
def zeige_auswahl():
    print("Ausgewählt:", auswahl.get())

# Hauptfenster erstellen
root = tk.Tk()
root.title("Radiobutton Beispiel mit IntVar")

# IntVar wird verwendet, um die Auswahl der Radiobuttons zu speichern
# Anfangswert -1 bedeutet: Kein Button ist ausgewählt
auswahl = tk.IntVar()
auswahl.set(-1)  # Kein Radiobutton ist am Anfang ausgewählt

# Radiobuttons erstellen
# Jeder Button bekommt einen eindeutigen Integer-Wert (z.B. 1, 2, 3)
rb1 = tk.Radiobutton(root, text="Option 1", variable=auswahl, value=1, command=zeige_auswahl)
rb2 = tk.Radiobutton(root, text="Option 2", variable=auswahl, value=2, command=zeige_auswahl)
rb3 = tk.Radiobutton(root, text="Option 3", variable=auswahl, value=3, command=zeige_auswahl)

# Die Buttons im Fenster anzeigen
rb1.pack()
rb2.pack()
rb3.pack()

# Hauptloop starten
root.mainloop()


"""
import tkinter as tk

# Funktion zur Anzeige der Auswahl
def zeige_auswahl():
    print("Newsletter:", newsletter_var.get())      # 1 = Ja, 0 = Nein
    print("AGB akzeptiert:", agb_var.get())          # 1 = Ja, 0 = Nein
    print("Werbung erhalten:", werbung_var.get())    # 1 = Ja, 0 = Nein

# Hauptfenster erstellen
root = tk.Tk()
root.title("Checkbuttons mit IntVar")

# Für jeden Checkbutton wird eine eigene IntVar verwendet
# Anfangswert ist 0 → nicht ausgewählt
newsletter_var = tk.IntVar()
agb_var = tk.IntVar()
werbung_var = tk.IntVar()

# Checkbuttons erstellen – jeder bekommt eine eigene Variable
cb1 = tk.Checkbutton(root, text="Newsletter abonnieren", variable=newsletter_var)
cb2 = tk.Checkbutton(root, text="AGB akzeptieren", variable=agb_var)
cb3 = tk.Checkbutton(root, text="Werbung erhalten", variable=werbung_var)

# Buttons anzeigen
cb1.pack(anchor="w")  # "w" = linksbündig
cb2.pack(anchor="w")
cb3.pack(anchor="w")

# Button zum Anzeigen der Auswahl
button = tk.Button(root, text="Auswahl anzeigen", command=zeige_auswahl)
button.pack(pady=10)

# Hauptloop starten
root.mainloop()
"""





