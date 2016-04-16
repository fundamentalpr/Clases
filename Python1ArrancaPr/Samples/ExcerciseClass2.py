#Python 3.3.0
#By Alfredo Alvarez
#Exercises class 2

def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)

def fibonacci(number):
    if number == 0 or number == 1:
        return 1
    else:
        return fibonacci(number - 1) * fibonacci(number - 2)
    
def get_factorial(n):
    if n >= 0:
        x = 1
        i = 0
        if n == 0:
            return 1
        else:
            while n > i:
                i = i + 1
                x = (x) * i
        return x
    else:
        raise ValueError("That's a negative number")
    
#recursive version
def getr_factorial(n):
    if n == 0 or n == 1:
        return 1
    if n < 0:
        raise ValueError("That's a negative number")
    return getr_factorial(n-1)*n

#Problem 2. Fibonacci
def get_fibonacci(n):
    if n == 0 or n == 1:
        return 1
    elif n >= 1:
        previousTolast = 1
        last = 1
        counter = 1
        while n > counter :
            counter += 1
            current = previousTolast + last
            previousTolast = last
            last = current         
        return last
    else:
        raise ValueError("That's a negative number")
    
#Problem 3. Reverse string
def reverse(s):
    str = ""
    l = []
    lenght = len(s)
    x = (lenght - 1)
    while x >= 0:
        l.append(s[x])
        x = x -1     
    return str.join(l)

#Problem 4. Write a function that removes the characters in a second string from the first.
def remove_oft(s, t):
    for char in t:      
            tmp = s.replace(char, '')
            s = tmp
    return s
    
#Problem 5. a function that returns true for odd numbers and false for even.

def is_odd(n):
    return n % 2 == 1
print("Testing odd")
print(is_odd(3) == True)
print(is_odd(4) == False)
print("Testing factorial")
print(get_factorial(0) == 1)
print(get_factorial(1) == 1)
print(get_factorial(3) == 6)
print("Testing recursive factorial")
print(getr_factorial(0) == 1)
print(getr_factorial(1) == 1)
print(getr_factorial(3) == 6)
print("Testing fibonacci")
print(get_fibonacci(0) == 1)
print(get_fibonacci(1) == 1)
print(get_fibonacci(3) == 3)
print(get_fibonacci(4) == 5)
print("Testing reverse")
print(reverse("sa") == "as")
print("Testing removal")
print(remove_oft("alfredo","fd")=="alreo")
