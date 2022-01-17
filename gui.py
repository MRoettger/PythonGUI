"""
Thinker Test File
"""
import tkinter as tk
from PIL import Image, ImageTk

#print('is this woking')

window = tk.Tk()
greeting = tk.Label(window, text="what's my favorite video?",
                 bg='#fff', fg='#f00', pady=10, padx=10, font=10)
greeting.pack()
#canvas = tk.Canvas(window, width=600,height=400)
#canvas.grid(columnspan=3)

#Logo
#logo = Image.open('1_52.png')
#logo = ImageTk.PhotoImage(logo)
#logo_lable = tk.Label(image=logo)
#logo_lable.image = logo
#logo_lable.grid(column=1, row=0)

#instructions
#instructions = tk.Label(window, text= "Select Somthing", font='Raleway')
#instructions.grid(columnspan=3,column=0,row=1)

window.mainloop()