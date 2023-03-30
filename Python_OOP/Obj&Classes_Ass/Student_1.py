"""Write a program to implement a class “student” with the following members. Name of the
student. Marks of the student obtained in three subjects. Function to assign initial values.
Function to compute total average. Function to display the student’s name and the total marks.
Write an appropriate main() function to demonstrate the functioning of the above."""


class Student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.maths = m1
        self.phy = m2
        self.chem = m3

    def find_avg(self):
        avg = (self.maths + self.chem + self.phy) / 3
        print("Average of the Subjects:", avg)

    def details(self):
        total = self.maths + self.chem + self.phy
        print(f"""Name of Student: {self.name}
Total Marks Of {self.name} is {total}""")


sam = Student('Sam', 90, 80, 75)
om = Student('Om', 90, 90, 85)

sam.details()
sam.find_avg()

input("Press Enter To Get Another Details")
om.details()
om.find_avg()
