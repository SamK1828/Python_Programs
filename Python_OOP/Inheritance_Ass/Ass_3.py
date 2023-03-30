"""A HighSchool application has two classes: the Person superclass and the Student subclass. Using
inheritance, in this lab you will create two new classes, Teacher and CollegeStudent. A Teacher
will be like Person but will have additional properties such as salary (the amount the teacher
earns) and subject (e.g. “Computer Science”, “Chemistry”, “English”, “Other”). The
CollegeStudent class will extend the Student class by adding a year (current level in college) and
major (e.g. “Electrical Engineering”, “Communications”, “Undeclared”)."""


class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, college_name, faculty):
        super().__init__(name)
        self.college_name = college_name
        self.faculty = faculty


class College_Student(Student):
    def __init__(self, name, college, faculty, year, branch):
        super().__init__(name, college, faculty)
        self.year = year
        self.branch = branch

    def show_details(self):
        print(f"""\nStudent Name: {self.name}
Student College: {self.college_name}
Student Faculty: {self.faculty}
Student Studying Year: {self.year}
Student Branch: {self.branch}\n""")


class Teacher(Person):
    def __init__(self, name, annual_salary, subject):
        super().__init__(name)
        self.salary = annual_salary
        self.sub = subject

    def show(self):
        print(f"""\nTeacher Name:{self.name}
Teacher Salary Per Month: {self.salary}
Teacher Subject: {self.sub}\n""")


s1 = College_Student("Samarth Deelip Kalegaonkar", "CSMSS CSCOE", "Engineering", '2nd', 'CSE')
t1 = Teacher("Anand Kumar", 40000, "Phy,Chem & Maths")
s1.show_details()
input("Enter to get Teacher Details...")
t1.show()
