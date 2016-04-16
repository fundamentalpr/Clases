#important to note that it defines a scope and that we are creating a function that creates another function
#think of it has a function template
def make_printer(msg):
    add = '7'
    def printer():
        print(msg + add)
    return printer

printer = make_printer('Value!')
printer()

printer2 = make_printer('Test2')
printer2()



def operation(symbol):
    def apply(first, second):
        if(symbol == "+"):
            return first + second
        elif(symbol == "-"):
            return first - second
        else:
            return " Fix your usage"
    return apply

sumop = operation("+")
subop = operation("-")
op3 = operation("l")


print(sumop(5,3))
print(subop(5,3))
print(op3(5,3))
