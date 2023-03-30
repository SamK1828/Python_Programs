class circle:
    def __init__(self, r):
        self.radius = r
        self.area = 0

    def print_area(self):
        self.area = 3.14 * self.radius ** 2
        print("Area Calculated:", self.area)


ob1 = circle(1.5)
ob1.print_area()
ob2 = circle(1.2)
ob2.print_area()
