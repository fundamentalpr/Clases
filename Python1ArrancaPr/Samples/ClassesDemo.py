#Created by alfredo alvarez
# demo of a class basic principlpes

#example class
class ExampleClass:
    #standard defiition of constructor(initializer) with one parameter
    def __init__(self, string):
        self.text = string
    #Example of a method being called.
    def invokeMethod(self):
        print("Hello "+self.text)

#using the class we first initialize
a = ExampleClass("Alfredo")
b = ExampleClass("Tyson")
c = [a,b]
#method being called
for item in c:
    item.invokeMethod()
#property being called
print(a.text)

        
    
