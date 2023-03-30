class Date:
    def __init__(self, day, month, year):
        self.d = day
        self.y = year
        self.m = month

    def show(self):
        print(f"{self.d}/{self.m}/{self.y}")

    @staticmethod
    def check(day, month, year):
        if 1 <= day <= 31:
            return True
        else:
            return False

    @classmethod
    def in_String(cls, s):
        arr = list(map(int, s.split("-")))
        # call init method of class
        t1 = cls(arr[0], arr[1], arr[2])
        return t1


ob1 = Date(12, 3, 22)
ob1.show()
print()
ob2 = Date.in_String("23-03-23")
ob2.show()


if Date.check(22, 2, 22):
    print("Valid Date...")
else:
    print("Invalid Date...")
