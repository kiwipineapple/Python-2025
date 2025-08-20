import tkinter as tk

def update_label(value):
    print("reached", value)
    label.config(text=scale_var.get())

root = tk.Tk()

scale_var = tk.DoubleVar()
scale = tk.Scale(root, variable=scale_var, from_=0.0, to=10.0, orient=tk.HORIZONTAL, resolution=0.1, command=update_label)
scale.pack()

label = tk.Label(root, text="0.0")
label.pack()

root.mainloop()
