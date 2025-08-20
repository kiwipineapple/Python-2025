import tkinter as tk


def zeige_statuts():
    status1 = 'An' if zustand1.get() else 'Aus'
    status2 = 'An' if zustand2.get() else 'Aus'
    label.config(
        text=f'checkbutton1: {status1}, checkbutton2: {status2}')


root = tk.Tk()
root.title('Checkbutton')
root.geometry('500x300')

zustand1 = tk.BooleanVar()
zustand2 = tk.BooleanVar()
# zustand.trace('w', on_change)

checkbutton1 = tk.Checkbutton(
    root, text='checkbutton1', variable=zustand1, command=zeige_statuts)
checkbutton1.pack()

checkbutton2 = tk.Checkbutton(
    root, text='checkbutton2', variable=zustand2, command=zeige_statuts)
checkbutton2.pack()

label = tk.Label(root)
label.pack()

root.mainloop()
