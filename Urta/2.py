class Restarn:
    def __init__(self, name: str) -> None:
        self.name = name
        
    def get_info(self):
        return f"{self.name} --> menyusi:"
    
class FastfFood(Restarn):
    def __init__(self, ism):
        self.ism = ism
    
    def get_in(self):
        return f"{self.ism} --> menyusi"
    
a = Restarn("Almaz")
b = FastfFood("Milaris")

print(a.get_info())
print(b.get_in())