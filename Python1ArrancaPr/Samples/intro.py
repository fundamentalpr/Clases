import sys

#__name gets assigned by the shell it is main when its the first file.
print(__name__)
#This wont print when i run

if __name__ == "__main__":
    print(sys.version)
    print("HEllo World")
    print("Hello human may i have your name?")
    OfficeDogName = "JAck"
    text = input()
    print("Thanks how was your day")
    text2 = input()
    print(text + " Glad that your day was: "+ text2)
    print(OfficeDogName)
    number = 5
    number2 = 7
    number3 = str(5) + str(7)
    print(number3)
