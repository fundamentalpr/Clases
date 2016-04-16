#Alfredo Alvarez
#python 3.3
#opening a file for write
f = open('myfile', 'w')
print(f)
#writing to the file myfile
f.write("Name: Alfredo")
f.write("\n Profession: Software Developer")
#closes teh file
f.close()
#look for this file on the folder where you loaded this file.
#Demo of reading the file we just wrote
f2 = open('myfile', 'r') # r+ read and write open
print(f2.readline()) # reads one line
f2.close()
f3 = open('myfile', 'r') # r+ read and write open
print(f3.read()) #reads quantity specified no param reads entire file
f3.close()

