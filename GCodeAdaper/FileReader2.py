import time

filename = "C:/Users/asus/Desktop/Python101/GC.gcode"
#filename = "hello.txt"
word = input("What do you want to find?\n")

start_time=time.time()
file = open(filename, "r")
content = file.readlines()
file.close()
end_time = time.time() - start_time
print("Read Time "+str(end_time))
#print(content)

#vars
counter = 0
lines =0
initLayer = False
#Analyze the content
start_time=time.time()
fout = open("helloOut.txt", "w")
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
end_time = time.time() - start_time

print("Write and Analyze Time "+str(end_time))
print(word+" Founded "+str(counter)+" times!")
print(str(lines)+" Lines")
