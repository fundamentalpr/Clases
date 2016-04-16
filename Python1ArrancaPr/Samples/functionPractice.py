def isOdd(number):
    if number % 2 != 0:
        return True
    else:
        return False

# factorial is the result of the multiplication of all the numbes
#till the number input
def factorial(number):
    collector = 1
    for i in range(1,number):
        collector = collector * i
    return collector

print(isOdd(3))



print(range(10))

print(factorial(2))
print(factorial(3))
