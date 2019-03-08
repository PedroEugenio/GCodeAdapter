################################
#  DEVELOPED BY PEDRO EUGÉNIO  #
################################
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox

# TODO
# - INSERT THE SPECIFIC GCODE TO RUN AFTER THE LAYER CHANGE
# - ADJUST Y AND X POSITION FROM GUI
# - CHECK BOX TO CHOOSE THE POSITION OF THE CAMERA
# __________________________________________________________

window = tk.Tk()
window.title("GUI-GCode Adapter")
window.geometry('500x600')
window.resizable(width=True, height=False)

delayTime = 500
retractionLength = 13
content = None
path = None
# ----Functions----
def getPath():
    return str(filedialog.askopenfilename(title="Select File", filetypes=(
    ("GCode files", "*.gcode"), ("Text Files", "*.txt"), ("all files", "*.*"))))


def browsefunc():
    global path
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
        if word in x and initLayer == True:
            counter += 1
            content.insert(i + 1, "G91; Put in relative mode\n"
                                  "G1 F3000 E-"+str(retractionLength)+"; retract\n"
                                  #"G1 F5000 Z5; Lower bed by 10mm\n"
                                  "G90; Put in absolute mode\n"
                                  "G1 F9000 X0 Y232.0; Back Home\n"
                                  "G4 P"+str(delayTime)+"; Wait\n"
                                  #"G91; Put in relative mode\n"
                                  #"G1 F3000 E10; extrude\n"
                                  #"G1 F5000 Z-5; Raise the bed back up 10mm\n"
                                  "G90; Put back in absolute mode\n"
            )
            # print("Word Position: "+str(i))
        fout.write(content[i])
    fout.close()


def showfunc():
    if content is None:
        messagebox.showerror("Error", "No file selected")
    else:
        contentText.insert('1.0', content)


def savefunc():
    processFile(content)
    messagebox.showwarning("Save File", "File Saved Successfully")

def clearfunc():
    contentText.delete("1.0","end")
    global path
    path = None
    filename.set("")
    global content
    content = None

def setfunc():
    global delayTime
    global retractionLength
    if delayTimeText.get().isdigit():
        delayTime = delayTimeText.get()
    if retractionText.get().isdigit():
        retractionLength = retractionText.get()
    print(delayTime,retractionLength)

# ----Frames----
topFrame = tk.Frame(window, relief=RAISED,borderwidth=1)
topFrame.pack(side=TOP, fill=BOTH, expand=True, padx=10,pady=10)

middleTopFrame = tk.Frame(topFrame)
middleTopFrame.pack(side=BOTTOM, padx=10)

middleFrame = tk.Frame(window)
middleFrame.pack(side=TOP,padx=10,fill=BOTH, expand=True)

bottomFrame = tk.Frame(window, relief=SUNKEN,borderwidth=2)
bottomFrame.pack(side=LEFT, pady=20, padx=10)


# ----Labels----
title = tk.Label(topFrame, text="GUI-GCode Adapter by Pedro Eugénio",justify=CENTER)
title.config(font=("Courier", 15))
#title.grid(column=1, row=0)
title.pack(side=TOP,pady=10)

setButton = tk.Button(middleTopFrame, text="Set", command=setfunc)
#loadButton.grid(column=0, row=1,columnspan=2)
setButton.pack(side=BOTTOM,fill=BOTH,expand=True, pady=10,padx=10)

delayLabel = tk.Label(middleTopFrame, text="Delay Time: ")
delayLabel.pack(side=LEFT,pady=10)
# ----Entry----
delaystr=StringVar(middleTopFrame,str(delayTime))
delayTimeText = tk.Entry(middleTopFrame,textvariable=delaystr)
delayTimeText.pack(side=LEFT)

retractionLabel = tk.Label(middleTopFrame, text="Retraction Length (mm): ")
retractionLabel.pack(side=LEFT,pady=10)
# ----Entry----
retstr=StringVar(middleTopFrame,str(retractionLength))
retractionText = tk.Entry(middleTopFrame, textvariable=retstr)
retractionText.pack(side=LEFT)




filename = tk.StringVar()
pathlabel2 = tk.Label(bottomFrame, textvariable=filename)
#pathlabel2.grid(column=1, row=1)
pathlabel2.pack(side = TOP)

# ----Buttons----
loadButton = tk.Button(middleFrame, text="Load", command=browsefunc)
#loadButton.grid(column=0, row=1,columnspan=2)
loadButton.pack(side = LEFT,fill=BOTH,expand=True)

showButton = tk.Button(middleFrame, text="Show File", command=showfunc)
#showButton.grid(column=0, row=2,columnspan=2)
showButton.pack(side = LEFT,fill=BOTH,expand=True)

saveButton = tk.Button(middleFrame, text="Save", command=savefunc)
#saveButton.grid(column=0, row=3, columnspan=2)
saveButton.pack(side = LEFT, fill=BOTH,expand=True)

clearButton = tk.Button(middleFrame, text="Clear", command=clearfunc)
#saveButton.grid(column=0, row=3, columnspan=2)
clearButton.pack(side = LEFT, fill=BOTH,expand=True)

# ----Text----
scrollBar=tk.Scrollbar(bottomFrame)
scrollBar.pack(side=RIGHT, fill=Y, pady=10)
contentText = tk.Text(bottomFrame, height=20, yscrollcommand=scrollBar.set)
#contentText.grid(column=1, row=2)
contentText.pack(side=LEFT,fill=BOTH, expand=True, pady=10)
scrollBar.config(command=contentText.yview)



window.update_idletasks()
print(window.winfo_width())

window.mainloop()
