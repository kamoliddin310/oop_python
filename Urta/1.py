class School:
    students = []

    def __init__(self, name: str) -> None:
        self.name = name

    def add_student(self, student: str) -> None:
        self.students.append(student)

    def delete_student(self, student: str) -> None:
        self.students.remove(student)

s = School("school21")
s.add_student("Lazizbek")
s.add_student("Diyorbek")

s.delete_student("Lazizbek")

print(s.students)