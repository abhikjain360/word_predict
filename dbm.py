from tkinter import *

def makeGUI():
    #main GUI window
    mainWindow = Tk(screenName=":0")
    mainWindow.geometry("700x410")
    mainWindow.configure(bg="#151515")

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

    predictions.insert(0, "test")

    mainWindow.mainloop()

if __name__ == "__main__":
    makeGUI()