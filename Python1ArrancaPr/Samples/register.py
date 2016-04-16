
control = ""
index = 0
listOfItems = []
while(control != "-done"):
    print("Give me a student name:")
    control = input()
    if(control != "-done"):
        listOfItems.append(control)
        index = index + 1

print("printing all the values")
for name in listOfItems:
    print(name)

print("How many students registered")
count = 0
for item in listOfItems:
    count = count +1
print(count)
