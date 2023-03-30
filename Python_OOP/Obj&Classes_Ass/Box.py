"""Write a class “Box” that with three member-variables “height”, “width” and “breadth”. Write
suitable constructors to initialize them. Add functions like “getVolume” and “getArea” that will
return volume and surface area respectively. Create object of boxes and then print their volume
and surface area."""


class Box:
    def __init__(self, h, w, b):
        self.height = h
        self.width = w
        self.breadth = b

    def get_vol(self):
        vol = self.height * self.width * self.breadth
        return vol

    def get_area(self):
        h = self.height
        w = self.width
        b = self.breadth
        area = 2 * (b * w + b * h + h * w)
        return area


box1 = Box(1, 2, 6)
volume_1 = box1.get_vol()
area_1 = box1.get_area()
print("Volume of Box 1 is:", volume_1)
input("Enter to Get Area Of the Box....")

print("Area of Box 1 is:", area_1)
