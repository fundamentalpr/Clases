def firstFunction(throwError):
    if throwError:
        raise ValueError("showing the error functionality")
    else:
        print("function works yeah")


def addHello(name):
    print("Welcome to the class: " + name)

studentList = ["Davin", "Sarah", "Louie", "Aaron"]

for var in studentList:
    addHello(var)


def multiplyBy4(first , second):
    return (first + second) * 4

result = multiplyBy4(10,20)
print(result)

print(addHello(str(multiplyBy4(10,20))))
