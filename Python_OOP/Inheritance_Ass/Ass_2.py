"""Create a class called Person with a member variable name.
Create a class called Employee who will inherit the Person class.The other data members of the
employee class are annual salary (double), the year the employee started to work, and the
national insurance number which is a String.
"""


class Person:
    def __init__(self, n):
        self.name = n


class Employee(Person):
    def __init__(self, name, salary, year, id):
        super().__init__(name)
        self.salary = salary
        self.year = year
        self.id = id

    def show_details(self):
        print(f"""\nEmployee Name: {self.name}
Employee Annual Income: {self.salary}
Employee Joining Year: {self.year}
Employee National Insurance Number: {self.id}\n""")


e1 = Employee("Samarth Kalegaonkar", 150000.00, 2022, 'CD987654A')
e1.show_details()
input("Press Enter to Get Details of Another Employee....")
e2 = Employee("Shreyash Kalegaonkar", 250000.00, 2028, 'EF246810B')
e2.show_details()
