print("Tell me the name of your file?")
filename = input()
f = open(filename +".txt",'r')
print(f.read())
