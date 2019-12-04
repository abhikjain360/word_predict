'''
import libraries :
    1. sqlite for database of words
    2. tkinter for GUI of the app
'''
import sqlite3
from tkinter import *

#method to make connection with database and return a cursor to execute commands
def establishConnection():
    #establishing connection with database
    conn = sqlite3.connect('words.db')

    #setting a cursor to execute database queries
    cursor = conn.cursor()

    return cursor

def makeGUI():
    #main GUI window
    mainWindow = Tk(screenName=":0")
    mainWindow.geometry("700x410")
    mainWindow.configure(bg="#151515")

    sv = StringVar(mainWindow)

    #configuring columns for the grif
    mainWindow.grid_columnconfigure(0, weight=1)
    mainWindow.grid_columnconfigure(1, weight=1)
    mainWindow.grid_columnconfigure(2, weight=1)

    #configuring rows for the grid
    for i in range(16):
        mainWindow.grid_rowconfigure(i, weight=1)

    #predictions listbox: to display predictions
    predictions = Listbox(mainWindow, bg="#636363", bd=0, font="verdana 14", height=18)
    predictions.grid(row=1, column=0, padx=10)

    #word entry: to get input
    word = Entry(mainWindow, bg="#B3B3B3", bd=2, font="verdana 14", fg="black", relief=FLAT, width=20, 
                    textvariable=sv)
    word.grid(row=0, column=0, padx=10, pady=10)

    #viewer text: to display text
    viewer = Text(mainWindow, bg="white", bd=0, font="monospaced 14", width=40, height=21)
    viewer.grid(row=0, column=1, rowspan=2, pady=10)

    #infinite loop for mainWindow untill stopped by the user
    mainWindow.mainloop()

    #returning StringVar to get input in main function
    return sv

#method to make predictions and print them to listbox
def getPredictions(s, cursor):
    cursor.execute(f"SELECT word FROM unigram_freq WHERE word LIKE '{s}%' ;")
    return cursor.fetchall()

def main():
    establishConnection()

    sv = makeGUI()

if __name__ == "__main__":
    main()