#python 3.3.0
#By Alfredo Alvarez
#Demo of regular expression usage.

import re
#Usage substitution only replaces those at the end   
print(re.sub('Alvarez$' , 'Mr. Broseph', "Hello Alvarez Alvarez"))
#Does not get substituted because its not at the end of the string
print(re.sub('Alvarez$' , 'Mr. Alvarez', "Alvarez Hello"))
#chaging the expression re can pick things in the beggining.
print(re.sub('^Hello' , 'Welcome', "Hello Alvarez"))

#How to use it for validation purposes
#two options
#Compiling and expression to use has validator
#string with 3 aaa and nothing else
#if not equal to none means that its a valid string
matcher = re.compile('^[a]{3}$')
print(matcher.match('aaa'))
print(matcher.match('aaa_'))
#Same thing different way of writing it
print(re.match('^[a]{3}$','aaa'))

#Using the search operation tells you the position The difference between match and search is that match always starts at the beginning of the string
print(re.match('A' ,  "Hello Alvarez"))
print(re.search('A' ,  "Hello Alvarez"))

#All regular expressions get cached which after awhile might take a lot of memory use purge to clean it
re.purge()

#Look on the presentation for a lot more demos this are incredibly powerful  notorious for creating bugs when misused

typed = input()
matched = re.match('^[0-9]{1,4}.[0-9]{2}$' ,  typed)
#matched = re.match('^[a-z0-9_-]{3,16}@[a-z0-9_-]{3,16}.com$' ,  typed)
if(matched != None):
    print("Valid Input")


