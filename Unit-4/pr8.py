from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): 
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def set_width(self, width):
        if width > 0:
            self.__width = width
        else:
            print("Width must be positive!")

    def area(self):
        return self.__width * self.__height

rect=Rectangle(5, 3)
print("Area:", rect.area())

rect.set_width(10)
print("New Area:", rect.area())

rect.set_width(-4)