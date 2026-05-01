"""
This is for showing the usage of multiple classes in one file 
"""

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self):
        return self.grade
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = list()
    
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            print(f"student {student.name} was added successfully to the course")
            return True
        return False

    def get_average_grade(self):
        total = 0
        for student in self.students:
            total += student.get_grade()
        return total / len(self.students)
    
s1 = Student("ismail", 26, 18)
s2 = Student("Nizar", 25, 18)
s3 = Student("Taha", 25, 18)

course = Course("Math", 2)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)  # Not added

print(f"{course.get_average_grade():.2f}")



