"""Create a class “Room” which will hold the “height”, “width” and “breadth” of the room in three
fields(variables). This class also has a method “volume()” to calculate the volume of this room."""


class Room:
    def __init__(self, h, w, b):
        self.height = h
        self.width = w
        self.breadth = b

    def show_values(self):
        print(f"""Height:{self.height}
Width: {self.width}
Breadth: {self.breadth}""")

    def find_vol(self):
        vol = self.height * self.width * self.breadth
        print("Volume of given Room is:", vol)


room1 = Room(100, 20, 15)
room2 = Room(222, 33, 25)
room1.show_values()
room1.find_vol()
print()
input("Enter to Get Details Of Another Room")
print()
room2.show_values()
room2.find_vol()
