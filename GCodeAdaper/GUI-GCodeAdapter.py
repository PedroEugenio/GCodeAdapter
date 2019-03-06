################################
#  DEVELOPED BY PEDRO EUGÉNIO  #
################################
import tkinter as tk
from tkinter import *
from tkinter import filedialog

# TODO
# - INSERT THE SPECIFIC GCODE TO RUN AFTER THE LAYER CHANGE
# - REDESIGN LAYOUT
# - ADJUST Y AND X POSITION FROM GUI
# - CHECK BOX TO CHOOSE THE POSITION OF THE CAMERA
# - SET THE RETRACTION SETTINGS
# - SET THE DELAY TIME
# __________________________________________________________

window = tk.Tk()
window.title("GUI-GCode Adapter")
window.geometry('500x500')
window.resizable(width=False, height=False)


# ----Functions----
def getPath():
    return str(filedialog.askopenfilename(title="Select File", filetypes=(
    ("GCode files", "*.gcode"), ("Text Files", "*.txt"), ("all files", "*.*"))))


def browsefunc():
    path = getPath()
    global content
    content = readFile(path)
    filename.set(path)


def readFile(filename):
    file = open(filename, "r")
    content = file.readlines()
    file.close()
    return content


def askForNameFileOut():
    return filedialog.asksaveasfilename(title="Save File",
                                 filetypes=(("GCode files", "*.gcode"), ("Text Files", "*.txt"), ("all files", "*.*")))

def processFile(content, fileOut="out.txt"):
    counter = 0
    lines = 0
    initLayer = False
    word = ";LAYER:"
    # Analyze the content
    filenameOut = str(askForNameFileOut())
    fout = open(filenameOut, "w")
    print(filenameOut+"\n")
    for i, x in enumerate(content):
        lines += 1
        if ";LAYER:0" in x:
            initLayer = True
            print("Find Initial Layer!")
        if word in x and initLayer == True:
            counter += 1
            content.insert(i + 1, "G91; Put in relative mode\n"
                                  "G1 F3000 E-13; retract\n"
                                  #"G1 F5000 Z5; Lower bed by 10mm\n"
                                  "G90; Put in absolute mode\n"
                                  "G1 F9000 X0 Y232.0; Back Home\n"
                                  "G4 P500; Wait"
                                  #"G91; Put in relative mode\n"
                                  #"G1 F3000 E10; extrude\n"
                                  #"G1 F5000 Z-5; Raise the bed back up 10mm\n"
                                  "G90; Put back in absolute mode\n"
            )
            # print("Word Position: "+str(i))
        fout.write(content[i])
    fout.close()


def convertfunc():
    contentText.insert('1.0', content)


def savefunc():
    processFile(content)

def clearfunc():
    contentText.delete("1.0","end")


# ----Frames----
topFrame = tk.Frame(window,width=window.winfo_width(), height=50)
topFrame.pack(side=TOP)
middleFrame = tk.Frame(window)
middleFrame.pack(side=TOP, pady=20)
bottomFrame = tk.Frame(window, relief=SUNKEN,borderwidth=2)
bottomFrame.pack(side=LEFT, pady=20, padx=10)
rightFrame = tk.Frame(window, relief=SUNKEN)
rightFrame.pack(side=LEFT, padx=30)

# ----Labels----
title = tk.Label(topFrame, text="GUI-GCode Adapter by Pedro Eugénio", relief=RAISED,borderwidth=2)
#title.grid(column=1, row=0)
title.pack(side=TOP,pady=5)

delayLabel = tk.Label(topFrame, text="Delay Time: ")
delayLabel.pack(side=LEFT,pady=5)

delayTimeText = tk.Entry(topFrame)
delayTimeText.pack(side=LEFT);

retractionLabel = tk.Label(topFrame, text="Retraction Length (mm): ")
retractionLabel.pack(side=LEFT,pady=5)
retractionText = tk.Entry(topFrame)
retractionText.pack(side=LEFT)

filename = tk.StringVar()
pathlabel2 = tk.Label(bottomFrame, textvariable=filename)
#pathlabel2.grid(column=1, row=1)
pathlabel2.pack(side = TOP)

# ----Buttons----
loadButton = tk.Button(middleFrame, text="Load", command=browsefunc)
#loadButton.grid(column=0, row=1,columnspan=2)
loadButton.pack(side = LEFT,fill=BOTH,expand=True)

convertButton = tk.Button(middleFrame, text="Convert", command=convertfunc)
#convertButton.grid(column=0, row=2,columnspan=2)
convertButton.pack(side = LEFT,fill=BOTH,expand=True)

saveButton = tk.Button(middleFrame, text="Save", command=savefunc)
#saveButton.grid(column=0, row=3, columnspan=2)
saveButton.pack(side = LEFT, fill=BOTH,expand=True)

clearButton = tk.Button(middleFrame, text="Clear", command=clearfunc)
#saveButton.grid(column=0, row=3, columnspan=2)
clearButton.pack(side = LEFT, fill=BOTH,expand=True)

# ----Text----
contentText = tk.Text(bottomFrame, height=20)
#contentText.grid(column=1, row=2)
contentText.pack(fill=BOTH, expand=True, pady=10)

# ----Entries----



window.update_idletasks()
print(window.winfo_width())

window.mainloop()
