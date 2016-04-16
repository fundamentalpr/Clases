#Alfredo Alvarez
#python 3.3
#opening a file for write
#f = open('myfile', 'w')
#print(f)
#writing to the file myfile
#f.write("Demoing python writing")
#closes teh file
#f.close()
#look for this file on the folder where you loaded this file.
#Demo of reading the file we just wrote
f2 = open('myfile', 'r') # r+ read and write open
print(f2.readline()) # reads one line
f2.close()
f3 = open('myfile', 'r') # r+ read and write open
f3.seek(3)
f3.seek(5)
print(f3.tell())
print(f3.read()) #reads quantity specified no param reads entire file
f3.close()

