import tkinter as tk


def zeige_auswahl():
    # print('Ausgewählt:', auswahl.get())
    label.config(text=f'Ausgewählt ist {auswahl.get()}')


root = tk.Tk()
root.title('Option Auswahl')
root.geometry('500x300')

auswahl = tk.StringVar()
auswahl.set(-1)


button1 = tk.Radiobutton(root, variable=auswahl, text='Option1',
                         value='Option1', command=zeige_auswahl)
button1.pack()

button2 = tk.Radiobutton(root, variable=auswahl, text='Option2',
                         value='Option2', command=zeige_auswahl)
button2.pack()

button3 = tk.Radiobutton(root, variable=auswahl, text='Option3',
                         value='Option3', command=zeige_auswahl)
button3.pack()

label = tk.Label(root)
label.pack()

root.mainloop()
