import tkinter as tk


def update(*args):
    print(entry.get())


root = tk.Tk()
root.geometry('400x300')

entry_variable = tk.StringVar()
entry_variable.trace('w', update)

entry = tk.Entry(root, textvariable=entry_variable, bg='lightblue')
entry.pack()

root.mainloop()
