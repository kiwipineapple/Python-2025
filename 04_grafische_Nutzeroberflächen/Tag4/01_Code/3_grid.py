import tkinter as tk

root = tk.Tk()
root.title("Raster-Beispiel")

# 🔧 Raster-Konfiguration (nur nötig, wenn sich Widgets beim Fenster-Resize mitvergrößern sollen)
# Spalte 1 erhält Gewicht 1 → kann sich mit dem Fenster mitvergrößern
root.grid_columnconfigure(1, weight=1)

# Zeile 1 erhält ebenfalls Gewicht → vertikales Mitwachsen möglich
root.grid_rowconfigure(1, weight=1)
root.configure(bg="lightblue")  # hellblauer Hintergrund für das ganze Fenster

"""
Diese Methode steuert, wie stark sich Spalten oder Zeilen mitvergrößern, 
wenn das Fenster größer gezogen wird.


weight=0 → fest
weight=1 → darf wachsen
weight=2+ → wächst stärker, je höher die Zahl
"""



# Erstellung der Widgets
label1 = tk.Label(root, text="Vorname:", bg="red")
label2 = tk.Label(root, text="Nachname:", bg="red")
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

def on_submit():
    print("Vorname:", entry1.get())
    print("Nachname:", entry2.get())

submit_button = tk.Button(root, text="Absenden", command=on_submit)

# Platzierung der Widgets im Raster mit Abstand und Ausrichtung
label1.grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry1.grid(row=0, column=1, padx=10, pady=10, sticky="we")
label2.grid(row=1, column=0, padx=10,pady=10, sticky="e")
entry2.grid(row=1, column=1, padx=10, pady=10, sticky="we")

submit_button.grid(row=2, column=0, columnspan=2, pady=10)
# Mehrere Zeilen/Spalten überspannen: Sie können rowspan und columnspan verwenden,
# um ein Widget mehrere Zeilen oder Spalten überspannen zu lassen.




root.mainloop()


"""
Der grid Geometriemanager in Tkinter wird verwendet, um Widgets in einer tabellenartigen Struktur 
innerhalb eines übergeordneten Containers zu organisieren

Grid: Der Container (wie ein Fenster oder ein Rahmen) ist in ein Raster aus Zeilen und Spalten unterteilt. 
Jede Zelle im Raster kann ein Widget enthalten.

Zeilen- und Spaltenindizes: Zeilen und Spalten werden ab 0 indiziert. 
Die Zelle oben links befindet sich also in Zeile 0, Spalte 0.

Sticky: Die sticky-Option wird verwendet, um anzugeben, an welche Seiten der Zelle das Widget haften soll. 
Sie kann Kombinationen der Werte n, s, e und w (für Norden, Süden, Osten und Westen) annehmen.

Abstand: Die Optionen padx und pady fügen zusätzlichen Platz um das Widget horizontal bzw. vertikal hinzu. 
ipadx und ipady fügen internen Abstand innerhalb des Widgets hinzu.
"""

