#generators in factorials note that generators are closures
def factorial(max):   
    a = 1
    b = 1          
    while a < max:
        yield b
        a += 1
        b = b * a


for value in factorial(25):
    print(value)
    
print(factorial(10))
