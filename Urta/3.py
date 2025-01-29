from pprint import pprint
class Student:
    def __init__(self, name: str, age: int, grades: list[int] = []) -> None:
        self.ism   = name
        self.yosh  = age
        self.baho  = grades
        
    def get_avg(self) -> float:
        return round(sum(self.baho) / len(self.baho), 2)
    
    def is_passing(self) -> bool:
        return self.get_avg() >= 60
                
a = Student("Aziz", 18, [80, 90, 70, 43, 65, 87, 54 ,90, 65])
b = Student("Ali", 12, [30, 40, 20, 45, 32, 21, 76, 87, 55, 98])
c = Student("Sherbek", 14, [90, 85, 95, 89, 97, 100, 87, 97])
d = Student("Asror", 17, [20, 10, 30, 65, 87, 98, 43, 32, 78, 87])

f = [            
    {"name": a.ism, "average": a.get_avg(), "passing": a.is_passing()},
    {"name": b.ism, "average": b.get_avg(), "passing": b.is_passing()},
    {"name": c.ism, "average": c.get_avg(), "passing": c.is_passing()},
    {"name": d.ism, "average": d.get_avg(), "passing": d.is_passing()},
]
pprint(f)


