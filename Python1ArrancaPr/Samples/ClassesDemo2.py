#Created by alfredo alvarez
# demo of a class basic principlpes


class PrintingProxy:
    def myprint(self, s):
        print(s)

class PrinterForTest:
    def __init__(self):
        self.text = ""
        
    def myprint(self, s):
        self.text = s

#example class
class ExampleClass:
    #standard definition of constructor(initializer) with one parameter
    def __init__(self, string, printingclass):
        self.text = string
        self.printer = printingclass
    #Example of a method being called.
    def invokeMethod(self):
        self.printer.myprint("Hello "+self.text)

#using the class we first initialize
a = ExampleClass("Alfredo", PrintingProxy())
b = ExampleClass("Tyson" , PrinterForTest())
print(a.printer)
print(b.printer)

c = [a,b]
#method being called
for item in c:
    item.invokeMethod()
    
print(b.printer.text)
if(b.printer.text == "Hello Tyson"):
    print("test: passed");
#property being called
print(a.text)



        
        
    
