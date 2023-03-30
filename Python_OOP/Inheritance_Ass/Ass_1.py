"""Create a class named ‘Animal’ which includes methods like eat() and sleep(). Create a child class
of Animal named ‘Bird’ and override the parent class methods. Add a new method named fly().
Create an instance of Animal class and invoke  eat and sleep methods using this object.
Create an instance of Bird class and invoke  eat, sleep and fly methods using this object."""


class Animal:

    def eat(self):
        print('Animal Eat Method')

    def sleep(self):
        print('Animal Sleep Method')


class Bird(Animal):
    def eat(self):
        print('Bird Eat Method')

    def sleep(self):
        print('Bird Sleep Method')

    def fly(self):
        print("Bird Fly Method")


b1 = Bird()
b1.fly()
b1.eat()
b1.sleep()
