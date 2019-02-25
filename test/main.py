class Polygon(object):
    def __init__(self, id):
        self.id = id
        print("Asda")


class Rectangle(Polygon):
    def __init__(self, id, width, height):
        super(self.__class__, self).__init__(id)
        self.shape = (width, height)


class Square(Rectangle):
    pass

p = Rectangle(1,2,3)
