import tkinter as tk

root = tk.Tk()
root.geometry('400x300')


def zeige_anweise():
    print(entry.get())


entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text='print',
                   command=zeige_anweise, highlightcolor='pink')
button.pack()

root.mainloop()
