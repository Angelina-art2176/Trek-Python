import math
from typing import Any

class Shape:

    def __init__(self, name: str) -> None:

        self.name: str = name
        self._created: bool = True

    def __str__(self) -> str:

        return f"Shape: {self.name}"

    def __repr__(self) -> str:

        return f"Shape(name={self.name!r})"

    def area(self) -> float:

        return 0.0

    def perimeter(self) -> float:

        return 0.0


class Circle(Shape):

    def __init__(self, radius: float) -> None:

        super().__init__("Circle")
        self.radius: float = radius

    def __str__(self) -> str:

        return f"Circle with radius {self.radius}"

    def __repr__(self) -> str:

        return f"Circle(radius={self.radius!r})"

    def area(self) -> float:

        return math.pi * self.radius ** 2

    def perimeter(self) -> float:

        return 2 * math.pi * self.radius

    def diameter(self) -> float:

        return self.radius * 2

if __name__ == "__main__":

    circle = Circle(5)

    print(circle)
    print(repr(circle))

    print("Area:", circle.area())
    print("Perimeter:", circle.perimeter())
    print("Diameter:", circle.diameter())