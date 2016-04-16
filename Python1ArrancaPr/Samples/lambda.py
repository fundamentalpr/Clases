#py 3.3
#alfredo Alvarez
# lambda expression create on the fly functions

#example using a func has variable

f = lambda x: x + x

print(f(2))

# which is useful because you can pass the function to other functions lamba mean the following is a function
def func(x):
    print("this is kinda cool")
    print(x())
    print("after it")

a = lambda : "Number1"   
func(a)
b= lambda : "Number2"
func(b)
    
#Helps build dictionaries examples keys mapped to an action
# they always need to return a value
def f2(x):
    return {
        'a': lambda : "Hey"+x,
        'b': lambda : "WOOT",
    }[x]
c = f2('a')
print(c())
d = f2('b')
print(d())


