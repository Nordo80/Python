"""Shapes."""


class Shape:
    """General shape class."""

    def __init__(self, color: str):
        """Constructor, sets the color."""
        self._color = color

    def set_color(self, color: str):
        """Set the color of the shape."""
        self._color = color

    def get_color(self) -> str:
        """Get the color of the shape."""
        return self._color

    def get_area(self) -> float:
        """Get area method which every subclass has to override."""
        return 0


class Circle(Shape):
    """Circle is a subclass of Shape."""

    def __init__(self, color: str, radius: float):
        """
        Constructor of the circle.

        The color is stored using superclass constructor:
        super().__init__(color)

        The radius value is stored here.
        """
        self._color = color
        self._radius = radius

    def __repr__(self) -> str:
        """
        Return representation of the circle.

        For this exercise, this should return a string:
        Circle (r: {radius}, color: {color})
        """
        return f"Circle (r: {self._radius}, color: {self._color})"

    def get_area(self) -> float:
        """
        Calculate the area of the circle.

        Area of the circle is pi * r * r.
        """
        return 3.14 * self._radius * self._radius


class Square(Shape):
    """Square is a subclass of Shape."""

    def __init__(self, color: str, side: float):
        """
        Constructor of the square.

        The color is stored using superclass constructor:
        super().__init__(color)

        The side value is stored here.
        """
        self._color = color
        self._side = side

    def __repr__(self) -> str:
        """
        Return representation of the square.

        For this exercise, this should return a string:
        Square (a: {side}, color: {color})
        """
        return f"Square (a: {self._side}, color: {self._color})"

    def get_area(self) -> float:
        """
        Calculate the area of the square.

        Area of the square is side * side.
        """
        return self._side * self._side


class Rectangle(Shape):
    """Square is a subclass of Shape."""

    def __init__(self, color: str, side1: float, side2: float):
        """
        Constructor of the square.

        The color is stored using superclass constructor:
        super().__init__(color)

        The side value is stored here.
        """
        self._color = color
        self._side1 = side1
        self._side2 = side2

    def __repr__(self) -> str:
        """
        Return representation of the square.

        For this exercise, this should return a string:
        Square (a: {side}, color: {color})
        """
        return f"Rectangle (l: {self._side1}, w: {self._side2}, color: {self._color})"

    def get_area(self) -> float:
        """
        Calculate the area of the square.

        Area of the square is side * side.
        """
        return self._side1 * self._side2


class Paint:
    """The main program to manipulate the shapes."""

    def __init__(self):
        """Constructor should create a list to store all the shapes."""
        self._list_list = []

    def add_shape(self, shape: Shape) -> None:
        """Add a shape to the program."""
        self._list_list.append(shape)

    def get_shapes(self) -> list:
        """Return all the shapes."""
        return self._list_list

    def calculate_total_area(self) -> float:
        """Calculate total area of the shapes."""
        total_area = 0
        for a in self._list_list:
            total_area += a.get_area()
        return total_area

    def get_circles(self) -> list:
        """Return only circles."""
        circle_list = []
        for a in self._list_list:
            if isinstance(a, Circle):
                circle_list.append(a)
        return circle_list

    def get_squares(self) -> list:
        """Return only squares."""
        square_list = []
        for a in self._list_list:
            if isinstance(a, Square):
                square_list.append(a)
        return square_list

    def get_rectangles(self) -> list:
        """Return only rectangles."""
        rectangle_list = []
        for a in self._list_list:
            if isinstance(a, Rectangle):
                rectangle_list.append(a)
        return rectangle_list


if __name__ == '__main__':
    paint = Paint()
    circle = Circle("blue", 10)
    circle2 = Circle("yellow", 13)
    square = Square("red", 11)
    rectangle = Rectangle("green", 8, 10)
    paint.add_shape(circle)
    paint.add_shape(square)
    paint.add_shape(circle2)
    print(paint.get_shapes())
    print(paint.calculate_total_area())
    print(paint.get_squares())
