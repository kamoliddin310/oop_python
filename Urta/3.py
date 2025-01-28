from pprint import pprint
class Student:
    def __init__(self, name: str, age: int, grades: list) -> None:
        self.ism   = name
        self.yosh  = age
        self.baho  = grades
        
    def get_avg(self):
        if len(self.baho) == 0:
            return 0
        return sum(self.baho) / len(self.baho)
    
    def is_passing(self) -> bool:
        return self.get_avg() > 60
                
a = Student("Aziz", 18, [80, 90, 70])
b = Student("Ali", 12, [30, 40, 20])
c = Student("Sherbek", 14, [90, 85, 95])
d = Student("Asror", 17, [20, 10, 30])

f = [            
    {"name": a.ism, "average": a.get_avg(), "passing": a.is_passing()},
    {"name": b.ism, "average": b.get_avg(), "passing": b.is_passing()},
    {"name": c.ism, "average": c.get_avg(), "passing": c.is_passing()},
    {"name": d.ism, "average": d.get_avg(), "passing": d.is_passing()},
]
pprint(f)


