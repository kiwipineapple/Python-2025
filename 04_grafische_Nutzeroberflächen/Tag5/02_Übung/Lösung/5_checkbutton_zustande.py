import tkinter as tk


def update_label():
    print(check_var1.get(), check_var2.get())
    status1 = "An" if check_var1.get() else "Aus"
    status2 = "An" if check_var2.get() else "Aus"
    label.config(text=f"Checkbutton 1: {status1}, Checkbutton 2: {status2}")


def main():
    root = tk.Tk()
    root.title("Checkbutton-Zustände anzeigen")

    global check_var1, check_var2, label
    check_var1 = tk.IntVar()
    check_var2 = tk.IntVar()

    checkbutton1 = tk.Checkbutton(root, text="Checkbutton 1", variable=check_var1, command=update_label)
    checkbutton1.pack(pady=5)

    checkbutton2 = tk.Checkbutton(root, text="Checkbutton 2", variable=check_var2, command=update_label)
    # ausprobiere mit onvalue und offvalue attributes
    checkbutton2.pack(pady=5)

    label = tk.Label(root, text="Checkbutton 1: Aus, Checkbutton 2: Aus")
    label.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()


"""
Erstelle eine Anwendung mit zwei Checkbuttons, die jeweils eine IntVar verwenden. Zeige den Zustand (an/aus) jedes Checkbuttons in einem Label an. Aktualisiere das Label jedes Mal, wenn sich der Zustand eines Checkbuttons ändert.


"""