from collections import deque
queue = deque(["Pineapple"])
queue.append("orange")   
print(len(queue))
queue.append("apple")
print(len(queue))
print(queue.popleft())    
print(len(queue))
