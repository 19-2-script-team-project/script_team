from tkinter import *
from tkinter.ttk import *
from tkinter.font import *

import random
import GUI

class Interface:
    def __init__(self):
        global L1
        window = Tk()
        
        self.frame1 = Frame(window)
        self.frame1.pack()

        frame2 = Frame(window)
        frame2.pack()
        L1 = Label(frame2, text = "게임중...")
        L1.pack()
        
        window.mainloop()


Interface()