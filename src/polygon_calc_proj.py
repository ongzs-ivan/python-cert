from abc import ABC, abstractmethod
import math

class Rectangle(ABC):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        pass

    def set_width(self, value):
        self.width = value

    def set_height(self, value):
        self.height = value

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return math.sqrt(self.width**2 + self.height**2)

    def get_picture(self):
        display = ''
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            for i in range(self.height):
                display += ("*" * self.width) 
                display += f'\n'
        return display

    def get_amount_inside(self, shape:"Rectangle"):
        return self.get_area() // shape.get_area()

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
        self.length = length

    def set_width(self, length):
        self.length = length
        self.width = length
        self.height = length

    def set_height(self, length):
        self.length = length
        self.width = length
        self.height = length

    def set_side(self, length):
        self.length = length
        self.width = length
        self.height = length

    def __str__(self):
        return f'Square(side={self.length})'

    
if __name__ == "__main__":
    # test run
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))