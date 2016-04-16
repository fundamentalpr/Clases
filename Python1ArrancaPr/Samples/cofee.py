class Coffee:
    def __init__(self, price, name):
        self.price = price
        self.name = name
        self.ingredients = []

    def giveMeThePrice(self, oz):
        return self.price * oz

class Menu:
    def __init__(self):
        self.MenuItem = []

    def print(self):
        print("*********MENU ITEMS *************")

        print("Name\t\tTall\tGrande")
        
        for item in self.MenuItem:
            print(item.name+"\t\t"+str(item.giveMeThePrice(12))+"\t"+str(item.giveMeThePrice(16)))

mocha =  Coffee(0.30, "Mocha")
chai = Coffee(0.28, "Chai Latte")
latte = Coffee(0.15, "Latte")
print("price of your mocha")
print( mocha.giveMeThePrice(12))
mocha.ingredients.append('Milk')
mocha.ingredients.append('Coffee')
mocha.ingredients.append('Chocolate')

for ing in mocha.ingredients:
    print(ing)

MyMenu = Menu()
MyMenu.MenuItem.append(mocha)
MyMenu.MenuItem.append(chai)
MyMenu.MenuItem.append(latte)
MyMenu.MenuItem.append(Coffee(0.10, "Drip"))
MyMenu.print()


