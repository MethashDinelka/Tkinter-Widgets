import tkinter as tk
from tkinter import ttk

root=tk.Tk()

width,height=300,200

display_width = root.winfo_screenwidth()
display_height = root.winfo_screenheight()

left = int((display_width/2) - (width/2))
top = int((display_height/2) - (height/2))

root.title("Labels 01")
root.geometry(f"{width}x{height}+{left}+{top}")
root.resizable(False,False)

label = ttk.Label(text="This is a Python Tkinter Program")
label.pack()

root.mainloop()