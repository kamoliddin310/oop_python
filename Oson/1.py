class Student:
    def __init__(self, ism, familiya, kurs, avg):
        self.name = ism
        self.last_name = familiya
        self.course = kurs
        self.avg = avg

    def fullname(self):
        return f"Assalomu alaykum mening ismim {self.name} {self.last_name}"
    
talaba = Student("Kamoliddin", "Jonxurozov", "2 - kurs", 89)

print(talaba.fullname())