"""
##### Task 1
Create a "Madlib" that has the users enter in a variety of noun/verb/adjectives.
When they press a button, it should update the contents of a label to display
the completed madlib.
What is a madlib? Visit https://www.madlibs.com/printables/ to see some Madlibs
you might use in your assignment
"""

import tkinter as tk 
from tkinter import *

win = tk.Tk()
win.geometry('600x400')
listword = ["Adjective", "Noun", "Holiday", "Person", "Place", "Verb", "Food", "Plural Noun", "Body part (Plural)"]
wordtype = StringVar()
output = StringVar()
label1 = tk.Label(win, text='Enter the next word.')
e1 = tk.Entry(win, width=20)
wtype=tk.Label(win,textvariable=wordtype)
label2=tk.Label(win,textvariable=output)
wordlist2=[]
wordtype.set(listword[0])
count=0

def displayMadLib():
    output.set("I can't believe it's already " + listword[2] + "! I can't wait to put on my " + listword[1] + " and visit every " + listword[4] + " in my neighborhood. This year, I am going to dress up as (a) " + listword[3] + " with " + listword[0] + " " + listword[8] + ". Before I " + listword[5] + ", I make sure to grab my " + listword[0] + " " + listword[1] + " to hold all of my " + listword[5] + ". Finally, all of my " + listwordp[6] + " are ready to go!")

def wordEntry():
    global count
    word=e1.get()
    word=str(word)
    wordlist2.append(word)
    e1.delete(0,END)
    
    count=count+1
    if count==10:
        print(len(wordlist2))
        displayMadLib()
        count=0

    
    wordtype.set(listword[count])
    
    length=len(wordlist2)
    




button1=tk.Button(win,text='Press to commit the word',command=wordEntry)

label1.grid(row=2,column=1)
e1.grid(row=2,column=2)
wtype.grid(row=1,column=2)
button1.grid(row=3,column=2)
label2.grid(row=5,column=1,columnspan=2)
win.mainloop()