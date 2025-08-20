import tkinter as tk


def update_statuts():
    if entry_variable.get():
        text.config(state=tk.NORMAL)
    else:
        text.config(state=tk.DISABLED)


root = tk.Tk()
root.title('Checkbutton')
root.geometry('500x300')

entry_variable = tk.BooleanVar()


text = tk.Text(root, width=40, height=1)
text.pack()


checkbutton = tk.Checkbutton(
    root, text='Eingabefeld aktivieren', variable=entry_variable, command=update_statuts)
checkbutton.pack()

root.mainloop()
