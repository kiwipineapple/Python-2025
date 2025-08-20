import tkinter as tk

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def update_label(*args):
    try:
        celsius = temp_var.get()
        fahrenheit = celsius_to_fahrenheit(celsius)
        label.config(text=f"Temperatur in Fahrenheit: {fahrenheit:.2f}")
    except tk.TclError:
        label.config(text="Bitte eine gültige Zahl eingeben")

def main():
    root = tk.Tk()
    root.title("Temperaturumrechnung")

    global temp_var, label
    temp_var = tk.DoubleVar()
    temp_var.trace_add("write", update_label)  # trace_add to monitor changes

    entry = tk.Entry(root, textvariable=temp_var)
    entry.pack(padx=10, pady=10)

    label = tk.Label(root, text="Temperatur in Fahrenheit: ")
    label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()

"""
Erstelle eine Anwendung mit einem Eingabefeld (Entry), in dem der Benutzer eine Temperatur 
in Celsius eingeben kann. Verwende eine DoubleVar(), um den Wert der Eingabe zu speichern. 
Füge ein Label hinzu, das die entsprechende Temperatur in Fahrenheit anzeigt,
 die automatisch aktualisiert wird, wenn der Benutzer den Wert ändert.


"""