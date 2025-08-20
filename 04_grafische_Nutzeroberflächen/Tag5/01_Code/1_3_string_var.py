import tkinter as tk

def update_label():
    label.config(text=entry_var.get())

root = tk.Tk()

entry_var = tk.StringVar()

entry = tk.Entry(root, textvariable=entry_var)
entry.pack()

button = tk.Button(root, text="Label aktualisieren", command=update_label)
button.pack()

label = tk.Label(root, text="Aktueller Wert")
label.pack()

root.mainloop()
