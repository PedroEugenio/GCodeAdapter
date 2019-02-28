import time

#fileName = input("File Name: ")
fileName = "GC.gcode"
print(fileName)
word = input("What do you want to find?\n")

f = open(fileName, "r+") #read and write
counter = 0
lines =0
start_time=time.time()
for x in f: #Lines
    lines +=1
    if word in x:
        lenX = len(x)
        print("String Length"+str(lenX))
        print("Word Position: "+str(x.index(word)))
        counter+=1
f.close()
end_time = time.time() - start_time

print("Find Time "+str(end_time))
print(word+" Founded "+str(counter)+" times!")
print(str(lines)+" Lines")


