import tkinter as tk

root = tk.Tk()
root.title('Benutzeroberfläche')
root.geometry('300x200')


def update_label():
    name = eingabe.get()
    Begruessung_text = f'Hallo {name}!'
    label2.config(text=Begruessung_text)


label1 = tk.Label(root, text='Bitte Name eingeben:')
label1.pack()

eingabe = tk.Entry(root)
eingabe.pack()

button = tk.Button(root, text='Gruessung', command=update_label)
button.pack()

label2 = tk.Label(root)
label2.pack()


root.mainloop()
