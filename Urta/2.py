class Restarn:
    menu = []
        
    def get_menu(self):
        return self.menu 
    
    def add_menu(self, food: dict):
        self.menu.append(food)
    
class FastfFood(Restarn):
    def menu_print(self):
        print("Menu:")
        for n, food in enumerate(self.menu, start=1):
            print(f"{n}. {food["name"]} - {food["price"]}")

class FineDining(Restarn):
     pass
    
a = FastfFood()
b = FineDining()

a.add_menu({'name': "Hotdog", "price": 15000})
a.add_menu({'name': "Shaurma", "price": 25000})

a.menu_print()