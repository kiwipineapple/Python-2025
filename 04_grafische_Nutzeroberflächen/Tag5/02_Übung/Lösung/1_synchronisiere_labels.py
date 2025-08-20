import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Synchronisiere zwei Labels")

    entry_var = tk.StringVar()

    entry = tk.Entry(root, textvariable=entry_var)
    entry.pack(pady=10)

    label1 = tk.Label(root, textvariable=entry_var)
    label1.pack(pady=10)

    label2 = tk.Label(root, textvariable=entry_var)
    label2.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()

"""
Erstelle eine Anwendung, in der zwei Labels denselben Text anzeigen, der in ein Eingabefeld eingegeben wird.
Verwende dafür eine StringVar, um den Text des Eingabefelds zu speichern und die Labels zu synchronisieren.

"""