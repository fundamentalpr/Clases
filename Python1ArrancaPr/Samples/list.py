name = "Hello"

for i in name:
    print(i)

#declaring a list
list = ["Charactes", 1 ,True]

for i in list:
    print(i)

#empty

print("HAndling the empty List")

list2 = []
print(len(list2))
list2.append("firstITem")
list2.append("secondITem")
print(len(list2))
#get a specific item from the list
print(list2[0])
print(list2[1])

list2.remove("firstITem")
print(len(list2))

#Queue operations
# they work in First IN First Out fashion

from collections import deque
queue = deque(["Pineapple"])
queue.append("orange")   
print(len(queue))
queue.append("apple")   
print(queue.popleft())    
print(len(queue))
print(queue.popleft())
print(queue.popleft())

print()
print("Stack")
print()
#stack operations
#LAst in first out
stack = ["Pineapple"]
stack.append("orange")   
print(len(stack))
stack.append("apple")   
print(stack.pop())    
print(len(queue))

