"""
use and import apartmenti4.py
apt.py
Chapter 8 EasyGUI
Author: William C. Gunnells
Rapid Python Programming
"""


# lib
from apartment4 import *
from easygui import *


myCo = Complex(10, 8, 1, 20, 15)
myCo.calc() 

data = []
for i in myCo.result():
    data.append(i+"\n")
textbox("apt data", "Apartment Complex", data)
