#File to demonstrate loops

#the while loop useful when u need to wait for a change before stopping the loop.
count = 0
while (count < 100):
   print(count)
   count = count + 1

#The for loop the bread and butter of looping
fruits = ['banana', 'apple',  'mango']
#any number in range will make it iterate that amount of times.
for index in range(len(fruits)):
   print('Current fruit :', fruits[index], index)

#iterating over a list
#we will cover lists later.
for letter in 'Python':     # First Example
   print('Current Letter :', letter)

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # Second Example
   print('Current fruit :', fruit)

 

