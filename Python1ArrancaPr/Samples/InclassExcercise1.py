
print("Tell me the name of your file?")
filename = input()
f = open(filename +".txt",'w')

control = ""
while(control != "-done"):
    print("Give me a student name:")
    control = input()
    if(control != "-done"):
        f.write(control)
        f.write("\n")

f.close()

