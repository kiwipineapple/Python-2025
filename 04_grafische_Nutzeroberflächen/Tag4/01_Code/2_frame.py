# Tkinter-Modul importieren
import tkinter as tk

# Funktion, die ausgeführt wird, wenn der Button geklickt wird


def on_button_click():
    print("Button clicked")  # Zur Kontrolle in der Konsole

    # Text aus dem Entry-Feld auslesen
    txt = entry.get()

    # Text aus dem Text-Widget auslesen (von Zeile 1, Zeichen 0 bis zum Ende)
    # .strip() entfernt das letzte \n
    textinhalt = text.get("1.0", "end").strip()

    # Ausgabe beider Texte in der Konsole (zur Demonstration)
    print("Entry:", txt)
    print("Textfeld:", textinhalt)

    # Anzeige im Label aktualisieren (z.B. kombiniert)
    display_Text.config(text=f"Name: {txt}\nNachricht: {textinhalt}")


# Hauptfenster erstellen
root = tk.Tk()  # Erzeugt das Hauptfenster der Anwendung
root.title("Simple Tkinter App")  # Setzt den Fenstertitel
root.geometry("500x300")  # Größe des Fensters in Pixeln (Breite x Höhe)

# Frame: Ein Container, um Widgets zu gruppieren

# Erster Frame (linke Seite)
# Erzeugt einen Rahmen im Hauptfenster mit grünem Hintergrund
frame_links = tk.Frame(root, bg="green")
# Positioniert den Frame auf der linken Seite des Fensters
frame_links.pack(side="left")

# Label: Zeigt statischen Text an
# Label mit dem Text "Willkommen"
label = tk.Label(frame_links, text="Willkommen")
label.pack(pady=20)  # Positioniert das Label mit vertikalem Abstand (Padding)

# Entry: Eingabefeld für einzeiligen Text
entry = tk.Entry(frame_links)  # Erzeugt ein Text-Eingabefeld
entry.pack(pady=40)  # Fügt es dem Frame hinzu mit vertikalem Abstand

# Text: Mehrzeiliges Textfeld
# Erzeugt ein größeres Textfeld (z.B. für längere Eingaben)
text = tk.Text(frame_links, height=5, width=40)
text.pack()  # Fügt es dem Frame hinzu

# Button: Führt bei Klick eine Aktion aus
button_widget = tk.Button(
    frame_links, text="Klick mich", command=on_button_click)
button_widget.pack(pady=20)  # Positioniert den Button mit vertikalem Abstand

# Label zur Anzeige der Benutzereingabe
# Leeres Label, das später aktualisiert wird
display_Text = tk.Label(frame_links, text="")
display_Text.pack(pady=10)


# Zweiter Frame (rechte Seite)
frame_rechts = tk.Frame(root, bg="lightgrey")
frame_rechts.pack(side="right", fill="both", expand=True)

# Weitere Widgets im zweiten Frame
label2 = tk.Label(frame_rechts, text="Dies ist der rechte Frame")
label2.pack(pady=20)

button2 = tk.Button(frame_rechts, text="Nur Deko")
button2.pack()


# Startet die Tkinter-Ereignisschleife – ohne diese bleibt das Fenster nicht offen
root.mainloop()
