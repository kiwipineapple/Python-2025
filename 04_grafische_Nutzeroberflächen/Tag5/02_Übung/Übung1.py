import tkinter as tk


# def update_label():
#     label1.config(text=entry_var.get())
#     label2.config(text=entry_var.get())


root = tk.Tk()

entry_var = tk.StringVar()

entry = tk.Entry(root, textvariable=entry_var)
entry.pack()

# button = tk.Button(root, text='aktualisieren', command=update_label)
# button.pack()

label1 = tk.Label(root, textvariable=entry_var)
label1.pack()

label2 = tk.Label(root, textvariable=entry_var)
label2.pack()

root.mainloop()
