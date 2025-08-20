# importieren
import tkinter as tk


# Jede Tkinter-Anwendung muss ein Hauptfenster erstellen.
# Dieses Hauptanwendungsfenster wird alle anderen GUI-Elemente beherbergen. So erstellen Sie es:
root = tk.Tk()

# legt den Titel des Hauptfensters der Anwendung auf "Einfache Tkinter-Anwendung" fest.
root.title("Einfache Tkinter-Anwendung")

# Widgets sind Elemente wie  Beschriftungen,Buttons, Textfelder usw.
# So fügen Sie Ihrem Hauptfenster ein einfaches Beschriftungsfeld und eine Schaltfläche hinzu:

# label ist ein Widget in der Tkinter-Bibliothek, das normalerweise verwendet wird,
# um Text oder Variablen in der Benutzeroberfläche anzuzeigen.
label = tk.Label(root, text="Hallo, Tkinter!")


"""
Die Methode pack() ist eine von drei Möglichkeiten, um Widgets im Fenster anzuordnen (neben grid() und place()).

Sie ist besonders einfach zu verwenden, da sie Widgets automatisch untereinander (vertikal) oder nebeneinander
(horizontal) anordnet — je nachdem, wie du es angibst. Ideal für schnelle Layouts ohne viel Aufwand.

Wenn du nichts weiter angibst, wird das Widget automatisch unter dem vorherigen platziert (side="top" ist Standard).

Möchtest du das Widget nebeneinander platzieren, verwende z. B. side="left" 
oder side="right" beim Aufruf von .pack(), Z.B. : label.pack(side="left")
"""
label.pack()

label_1 = tk.Label(root, text="Hallo, links!")
label_1.pack(side="left")

label_2 = tk.Label(root, text="Hallo, rechts!")
label_2.pack(side="right")

def update_label():
    # Die Methode config() wird hier benutzt, um die Konfiguration des Label-Widgets zu ändern.
    # Das bedeutet, dass der Text des Labels zu "Button geklickt!" geändert wird, sobald diese Funktion aufgerufen wird.
    label.config(text="Button geklickt!")

# Aufruf der Funktion update_label(), sobald der Benutzer auf diese Schaltfläche klickt
button = tk.Button(root, text="Klick mich", command=update_label)


button.pack()

# Um die Anwendung zu starten, müssen Sie die Methode mainloop für Ihr Hauptfensterobjekt aufrufen.
# Dies startet die GUI-Ereignisschleife.
root.mainloop()
