class Test:
    def instance_method(self):
        print("Instance Method Called......")

    @classmethod
    def class_method(cls):
        print("Class Method Called......")

    @staticmethod
    def static_method():
        print("Static Method Is Called.....")


ob1 = Test()
ob1.instance_method()
Test.class_method()
Test.static_method()
