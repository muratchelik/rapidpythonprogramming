"""
checkbutton.py
Chapter 9 Tkinter
Author: William C. Gunnells
Rapid Python Programming
"""


# lib
from tkinter import *

root = Tk()
root.geometry('200x50+250+50')
check = Checkbutton(root, bg='white',
                    text='Check 1',
                    font=('Helvatica',
                          20))
check.pack()
root.mainloop()
