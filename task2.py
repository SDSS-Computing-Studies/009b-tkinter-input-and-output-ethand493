"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""
import tkinter as tk
from tkinter import *
import math
window = tk.Tk()
eoutput = StringVar()
s = math.sqrt

def math():
    b,c = entry1.get(), entry2.get()
    b,c = float(b),float(c)
    x = float((b**2)-(4*c))
    x = s(x)
    x = x/2
    new = float((b**2) - (4*c))
    new = s(new)
    new = (-b)-new
    new = new/2
    math = []
    math.append(x)
    math.append(new)
    answer.delete(0,END)
    answer.insert(0,math)

label1 = tk.Label(window, text="Enter the B and C values into the equation \n then, press the equal button for the result.")
label2 = tk.Label(window, text="1 +")
entry1 = tk.Entry(window, width=5)
label3 = tk.Label(window, text="+")
entry2 = tk.Entry(window,width=5)
b1 = tk.Button(window, text="=", command=math)
entry3 = tk.Entry(window, width=5)
answer = Entry(window,width=10,textvariable=eoutput)

label1.grid(row = 1, column = 1)
label2.grid(row = 2, column = 2)
entry1.grid(row = 2, column = 3)
label3.grid(row = 2, column = 4)
entry2.grid(row = 2, column = 5)
b1.grid(row = 2, column = 6)
answer.grid(row = 2, column = 7)


window.mainloop()