class Student:
    school = "ABS School"

    def __str__(self):
        return f"name: {self.name}, score: {self.score}"

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def show_info(self):
        print(f"{self.name} score is {self.score}")

    def is_passed(self):
        return self.score >= 10

    def increase_score(self, x):
        self.score += x
        return self.score


class UniversityStudent(Student):
    def __init__(self, name, score, major):
        super().__init__(name, score)
        self.major = major


student = UniversityStudent("Ali", 18, "AI")
# student2 = Student("Mohammad", 8)

# print(student1.name)
# print(student1.age)
# print(student1.score)

# student1.show_info()
# student2.show_info()
print(student.is_passed())
# print(student2.is_passed())
print(student.increase_score(2))
# student1.school = "XYZ School"
# print(student1.school)
# print(student2.school)
# print(student1.name)
# print(student2.name)
print(student)
print(student.name)
print(student.score)
print(student.major)
