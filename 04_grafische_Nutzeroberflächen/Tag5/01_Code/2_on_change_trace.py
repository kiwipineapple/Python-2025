import tkinter as tk


def on_change(*args):
    #print(args)
    print("Variable geändert:", entry_var.get())


root = tk.Tk()

entry_var = tk.StringVar()
entry_var.trace("w", on_change)
# Die Funktion 'on_change' wird automatisch aufgerufen, wenn sich der Wert ändert
# "w" steht für "write" – wird ausgeführt, wenn der Wert geschrieben/geändert wird
# Weitere Optionen für trace():
# "r" = read     → wenn der Wert gelesen wird
# "w" = write    → wenn der Wert geändert wird (am häufigsten verwendet)
# "u" = undefine → wenn die Variable gelöscht wird

entry = tk.Entry(root, textvariable=entry_var)
entry.pack()

root.mainloop()



"""
Im Kontext der Tkinter trace-Methode ist der Parameter *args in der 
Callback-Funktion aus mehreren Gründen wichtig:

Umgang mit zusätzlichen Argumenten: Die trace-Methode übergibt 
zusätzliche Argumente an die Callback-Funktion, wenn sich die verfolgte Variable ändert. 
Genauer gesagt, werden drei Argumente übergeben:

Der Name der Variable.
Der Index der Variable.
Die durchgeführte Operation (entweder "lesen", "schreiben" oder "löschen").
Durch die Verwendung von *args kannst du sicherstellen, dass deine Callback-Funktion
 diese zusätzlichen Argumente akzeptieren kann, ohne sie explizit in der Funktionssignatur
  zu definieren. Dies macht deine Funktion flexibler und verhindert Fehler, die auftreten 
  würden, wenn diese Argumente nicht behandelt werden.

Ignorieren unnötiger Argumente: Oft benötigst du diese zusätzlichen Argumente in deiner 
Callback-Funktion nicht. Durch die Verwendung von *args kannst du sie effektiv ignorieren und 
trotzdem sicherstellen, dass die Funktion korrekt von der trace-Methode aufgerufen wird. 
Dies hält deine Funktionsdefinition einfach und konzentriert sich auf die eigentliche Aufgabe.

Ohne *args müsste die Funktion on_change diese Argumente explizit definieren und behandeln, 
selbst wenn sie nicht verwendet werden, wie folgt:
def on_change(var_name, index, operation):
    print("Variable geändert:", entry_var.get())

Die Verwendung von *args macht die Callback-Funktion jedoch prägnanter und flexibler:

def on_change(*args):
    print("Variable geändert:", entry_var.get())

Dieser Ansatz ist besonders nützlich bei der Arbeit mit Callbacks 
in Tkinter, bei denen die Bibliothek möglicherweise zusätzliche 
Informationen übergibt, die du für deinen speziellen Anwendungsfall nicht benötigst.

"""