import tkinter as tk

root = tk.Tk()
root.title("trace() Demo: w, r, u")
root.geometry("350x280")

# StringVar-Variable definieren (Kontroll-/Steuerelementvariable)
entry_var = tk.StringVar()

# Flag zur Kontrolle, ob der erste (automatische) Lesezugriff ignoriert werden soll
was_read_once = False

# --- trace-Funktionen ---

def on_write(*args):
    # "w" steht für "write": wird aufgerufen, wenn sich der Wert der Variable ändert
    if entry_var is not None:
        print("📝 Variable geändert (write):", entry_var.get())

def on_read(*args):
    # "r" steht für "read": wird aufgerufen, wenn der Wert gelesen wird
    global was_read_once
    if entry_var is not None:
        if was_read_once:
            print("📖 Variable wurde gelesen (read):", entry_var.get())
        else:
            was_read_once = True  # ersten automatischen Lesezugriff ignorieren
    else:
        print("⚠️ Hinweis: Variable ist nicht mehr vorhanden (None)")

def on_undefine(*args):
    # "u" steht für "undefine": wird aufgerufen, wenn die Variable gelöscht wird
    print("❌ Variable wurde gelöscht (undefine)")

# --- trace() aktivieren ---
entry_var.trace("w", on_write)
entry_var.trace("r", on_read)
entry_var.trace("u", on_undefine)

# --- GUI Elemente ---

# Eingabefeld (Entry), verbunden mit der Variable
entry = tk.Entry(root, textvariable=entry_var)
entry.pack(pady=10)

# Button zum Lesen des Variablenwerts (löst "r" aus)
def read_var():
    if entry_var is not None:
        print("Button hat gelesen:", entry_var.get())
    else:
        print("⚠️ Hinweis: Variable wurde gelöscht – kein Zugriff mehr möglich.")

btn_read = tk.Button(root, text="Wert lesen (r)", command=read_var)
btn_read.pack(pady=5)

# Button zum sicheren Löschen der Variable (löst "u" aus)
def delete_var():
    global entry_var
    entry.config(state="disabled")         # Entry-Feld deaktivieren
    entry.config(textvariable=None)        # Verbindung zur Variable trennen
    entry_var = None                       # Variable vollständig löschen
    print("✅ Variable gelöscht und Feld deaktiviert.")

btn_delete = tk.Button(root, text="Variable löschen (u)", command=delete_var)
btn_delete.pack(pady=5)

# Info-Label (optional)
tk.Label(root, text="Probiere Eingabe, Lesen, Löschen aus").pack(pady=15)

root.mainloop()
