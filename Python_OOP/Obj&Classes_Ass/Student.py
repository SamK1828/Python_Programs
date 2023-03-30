"""Create a class that captures students. Each student has a first name, last name, class year, and 
major. Create two examples of students"""


class Student:
    def __init__(self, fn, ln, year, major):
        self.fname = fn
        self.ln = ln
        self.year = year
        self.major = major

    def show_student(self):
        print("First Name", self.fname)
        print("Last name", self.ln)
        print("Class Year", self.year)
        print("Major", self.major)


s1 = Student('abc', 'xyz', 1, 'CSE')
s2 = Student('pqr', 'wsd', 2, 'CSE')
s1.show_student()
input("Enter")
s2.show_student()
