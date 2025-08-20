import tkinter as tk

def toggle_entry():
    if check_var.get():
        entry.config(state=tk.NORMAL)
    else:
        entry.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    root.title("Checkbox zum Umschalten von Widgets")

    global check_var, entry
    check_var = tk.BooleanVar()

    # Initialisiere das Eingabefeld als deaktiviert
    entry = tk.Entry(root, state=tk.DISABLED)
    entry.pack(pady=10)

    checkbutton = tk.Checkbutton(root, text="Eingabefeld aktivieren", variable=check_var, command=toggle_entry)
    checkbutton.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()


"""
Erstelle eine Anwendung mit einem Eingabefeld (Entry) und einem Kontrollkästchen (Checkbutton), das eine BooleanVar verwendet. Wenn das Kontrollkästchen aktiviert ist, sollte das Eingabefeld aktiviert (beschreibbar) sein. 
Wenn das Kontrollkästchen deaktiviert ist, sollte das Eingabefeld deaktiviert (nicht beschreibbar) sein.
"""