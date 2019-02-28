################################
## DEVELOPED BY PEDRO EUGÉNIO ##
################################
import tkinter as tk
from tkinter import filedialog

# TODO
# - INSERT THE SPECIFIC GCODE TO RUN AFTER THE LAYER CHANGE
# - REDESIGN LAYOUT
#__________________________________________________________

window = tk.Tk()
window.title("GUI-GCode Adapter")
window.geometry('400x500')

#----Functions----
def getPath():
    return str(filedialog.askopenfilename(title = "Select File",filetypes = (("GCode files","*.gcode"),("Text Files","*.txt"),("all files","*.*"))))

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
    filedialog.asksaveasfilename(title = "Save File",filetypes = (("GCode files","*.gcode"),("Text Files","*.txt"),("all files","*.*")))

def processFile(content, fileOut = "out.txt"):
    counter = 0
    lines =0
    initLayer = False
    word = "Z"
    #Analyze the content
    filenameOut = str(askForNameFileOut())
    fout = open(filenameOut, "w")
    for i,x in enumerate(content):
        if lines < 37:
            print(content[i])
        lines +=1
        if ";LAYER:0" in x:
            initLayer = True
            print("Find Initial Layer!")
        if word in x and initLayer == True:
            counter +=1
            content.insert(i+1,"Geno\n")
            #print("Word Position: "+str(i))
        fout.write(content[i])
    fout.close()

def convertfunc():
    contentText.insert('1.0',content)

def savefunc():
    processFile(content)

#----Labels----
title = tk.Label(window, text="GUI-GCode Adapter by Pedro Eugénio")
title.grid(column=1, row=0)

filename = tk.StringVar()
pathlabel2 = tk.Label(window, textvariable=filename)
pathlabel2.grid(column=1, row=1)
    
#----Buttons----
loadButton = tk.Button(window,text="Load", command=browsefunc)
loadButton.grid(column=0, row=1)

convertButton = tk.Button(window,text="Convert", command=convertfunc)
convertButton.grid(column=0, row=2)

saveButton = tk.Button(window,text="Save", command=savefunc)
saveButton.grid(column=0, row=3)

#----Text----
contentText = tk.Text(window, width=30, height=20)
contentText.grid(column=1, row=2)

#----Entries----

window.mainloop()
