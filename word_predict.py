#importing necceasy libraries
import sqlite3
import tkinter as tk

#establishing connection with database
conn = sqlite3.connect('words.db')

#setting a cursor to execute database queries
cursor = conn.cursor()

#GUI window
mainWindow = tk.Tk(screenName=":0")
mainWindow.geometry("700x400")

#frame on the right for word predictions
predictionsFrame = tk.Frame(mainWindow, height="400px", width="200px", bg="#11110e")
predictionsFrame.pack(side="right", fill="both")

#predictions listbox
predictions = tk.Listbox(predictionsFrame, bg="#5e5e5e")
predictions.insert(0,"Test0")
predictions.insert(1,"Test1")
predictions.insert(2,"Test2")
predictions.insert(3,"Test3")
predictions.pack(side="bottom", fill="x")

#starting the mainWindow
mainWindow.mainloop()