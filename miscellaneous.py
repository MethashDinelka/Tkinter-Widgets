import tkinter as tk
from tkinter import ttk

root=tk.Tk()

def click():
    label.configure(text=entry.get())
    print(entry.get())

width,height=600,350

display_width = root.winfo_screenwidth()
display_height = root.winfo_screenheight()

left = int((display_width/2) - (width/2))
top = int((display_height/2) - (height/2))

root.title("Miscellaneous [ Buttons+Labels+Entry]")
root.iconbitmap("cook.ico")
root.geometry(f"{width}x{height}+{left}+{top}")
root.resizable(False,False)

entry = ttk.Entry(root)
entry.pack()

button = ttk.Button(root,text="Click Here",command=click)
button.pack()

label = ttk.Label(root)
label.pack()
label.configure(text="Output Will Appear Here :)")

label2 = ttk.Label(root)
label2.pack()
label2.configure(text="* Look at the console for the output also.")

root.mainloop()