import tkinter as tk
from tkinter import ttk

root=tk.Tk()

width,height=300,200

display_width = root.winfo_screenwidth()
display_height = root.winfo_screenheight()

left = int((display_width/2) - (width/2))
top = int((display_height/2) - (height/2))

root.title("Buttons 01")
root.geometry(f"{width}x{height}+{left}+{top}")
root.resizable(False,False)

button = tk.Button(text="Welcome !")
button.pack()

button2 = ttk.Button(text="Have a nice day !")
button2.pack()

root.mainloop()