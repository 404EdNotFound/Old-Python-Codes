class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        area = self.width * self.height
        return print("Area: ", area)
        # TODO: calculate and return the area of the rectangle

    def perimeter(self):
        perimeter = (self.width * 2) + (self.height * 2)
        return print("Perimeter: ", perimeter)
        # TODO: calculate and return the perimeter of the rectangle

    def is_square(self):
        if self.width == self.height:
            return f"Number is square"
        # TODO: determine whether the rectangle is a square

class Square(Rectangle):
    def __init__(self, side_length):
        self.side_length = side_length
        # TODO: override the __init__ method to take a single argument for the length of the sides
        super().__init__(side_length, side_length)
    # The area, perimeter, and is_square methods should already work for squares because they inherit from the Rectangle class.

print("Features of the rectangle")
rectangle = Rectangle(4, 5)
rectangle.area()
rectangle.perimeter()

print("\n")
print("Features of a Square")
square = Square(4)
square.area()
square.perimeter()