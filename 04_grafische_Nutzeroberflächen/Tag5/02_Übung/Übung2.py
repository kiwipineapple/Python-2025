import tkinter as tk


def zeige_auswahl():
    print('Ausgewählt:', auswahl.get())


root = tk.Tk()
root.title('Geschlecht Auswahl')

auswahl = tk.StringVar()
auswahl.set(-1)


button1 = tk.Radiobutton(root, variable=auswahl, text='Weiblich',
                         value='Weiblich', command=zeige_auswahl)
button1.pack()
button2 = tk.Radiobutton(root, variable=auswahl, text='Männlich',
                         value='Männlich', command=zeige_auswahl)
button2.pack()

root.mainloop()
