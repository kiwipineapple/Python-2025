import tkinter as tk


def update_label():
    selected_option = option_var.get()
    if selected_option == "":
        label.config(text="Ausgewählte Option: Keine")
    else:
        label.config(text=f"Ausgewählte Option: {selected_option}")


def main():
    root = tk.Tk()
    root.title("Optionen mit Radiobuttons auswählen")

    global option_var, label
    option_var = tk.StringVar(value="unselected")
    # StringVar für die Auswahl definieren
    # Startwert ist "unselected", dieser passt zu keinem Radiobutton → also bleibt alles abgewählt

    radio1 = tk.Radiobutton(root, text="Option 1", variable=option_var, value="Option 1", command=update_label  )
    radio1.pack(pady=5)

    radio2 = tk.Radiobutton(root, text="Option 2", variable=option_var, value="Option 2", command=update_label )
    radio2.pack(pady=5)

    radio3 = tk.Radiobutton(root, text="Option 3", variable=option_var, value="Option 3", command=update_label)
    radio3.pack(pady=5)




    label = tk.Label(root, text="Ausgewählte Option: Keine")
    label.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()

"""
Erstelle eine Anwendung mit drei Radiobuttons, die eine StringVar verwenden, um die ausgewählte Option zu speichern. 
Zeige die ausgewählte Option in einem Label an.
Die Radiobuttons sollten verschiedene Textoptionen darstellen (z.B. "Option 1", "Option 2", "Option 3").
"""
