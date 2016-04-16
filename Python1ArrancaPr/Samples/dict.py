#define a dictionary
fruitsByColor = {"red": "apple", "blue": "berry"}
#retrieve the values
name =""
print(fruitsByColor["blue"])
while( name != "-done"):
    print("Enter student name to get their hobbies")
    name= input()

    HobbiesByPerson = {"Aaron":["Photography","Spelunking"],
                   "Sarah":["Climbing","Spelunking"]}
    if(name != "-done"):
        hobbies =  HobbiesByPerson[name]

    for h in hobbies:
        print(h)
print("We are done")
