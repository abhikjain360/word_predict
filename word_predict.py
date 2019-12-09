'''
import libraries :
    1. sqlite for database of words
    2. tkinter for GUI of the app
'''
import sqlite3
from tkinter import *
import time

#establishing connection with database
conn = sqlite3.connect('words.db')

#setting a cursor to execute database queries
cursor = conn.cursor()

#main GUI window
mainWindow = Tk(screenName=":0")
mainWindow.geometry("700x430")
mainWindow.configure(bg="#151515")

#configuring columns for the grif
mainWindow.grid_columnconfigure(0, weight=1)
mainWindow.grid_columnconfigure(1, weight=1)
mainWindow.grid_columnconfigure(2, weight=1)

#viewer text: to display text
viewer = Text(mainWindow, bg="white", bd=0, font="monospaced 14", width=40, height=21)
viewer.grid(row=0, column=1, rowspan=2, pady=10)

def clearViewer():
    viewer.delete(1.0, END)
    predictions.delete(0,END)
    word.delete(0, END)

clrBtn = Button(mainWindow, text="CLEAR", fg='red', command=clearViewer)
clrBtn.grid(row=2, column=1)

def onSelect(event):
    widg = event.widget
    index = int(widg.curselection()[0])
    value = str(widg.get(index)) + " "
    viewer.insert(END, value)

#predictions listbox: to display predictions
predictions = Listbox(mainWindow, bg="#636363", bd=0, font="verdana 14", height=18)
predictions.grid(row=1, column=0, padx=10)
predictions.bind("<<ListboxSelect>>", onSelect)

#String variable to get input
sv = StringVar()

#method to make predictions and print them to listbox
def getPredictions(s):
    cursor.execute(f"SELECT word FROM unigram_freq WHERE word LIKE '{s}%' ;")
    return cursor.fetchmany(15)

def StartInput():
    w = sv.get()
    s = getPredictions(w)
    predictions.delete(0,END)
    for i in s:
        predictions.insert(END, i[0])
    return True

#word entry: to get input
word = Entry(mainWindow, bg="#B3B3B3", bd=2, font="verdana 14", fg="black", relief=FLAT, width=20, 
            textvariable=sv, validate="key", validatecommand=StartInput)
word.grid(row=0, column=0, padx=10, pady=10)

#infinite loop for mainWindow untill stopped by the user
mainWindow.mainloop()
