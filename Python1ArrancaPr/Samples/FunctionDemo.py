#Example comment code written in python 3.3.0
#by Alfredo Alvarez

#Basic function demonstrates passing a parameter with no return value
def firstFunction(throwError):
    if throwError:
        raise ValueError("showing the error functionality")
    else:
        print("function works yeah")
    print("only run if error does not run")
    
#Basic function demonstrates passing two parameters with a return value
def secondFunctionWithReturnValue(operandone, operandtwo):
    return operandone + operandtwo

def recursiveFunction(operandOne):
    if operandOne == 0:
        return 1
    else:
        return recursiveFunction(operandOne-1) + recursiveFunction(operandOne-1) 
     



# If its not in a function the code will get executed when the module gets run
firstFunction(False)
# Should write in the console showing the function works yeah after running
firstFunction(True)
# Should demonstrate in red that it throws the value error.

#Shows passing more than one parameter and returns the value 2
secondFunctionWithReturnValue(1,1)
