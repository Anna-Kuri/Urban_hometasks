from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, color: tuple[int], *sides: int, filled: bool = True):
        self.__color = list(color)

        if len(sides) == self.sides_count:
            self.__sides = list(*sides)
        else:
            self.__sides = [*sides[0]] * self.sides_count

        self.filled = filled

    def get_color(self) -> list[int]:
        return self.__color

    def __is_valid_color(self, r: int, g: int, b: int) -> bool:
        for color in [r, g, b]:
            if color not in range(0, 256):
                return False
        return True

    def set_color(self, r: int, g: int, b: int) -> None:
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides) -> bool:
        if len(new_sides) != len(self.__sides):
            return False
        for side in new_sides:
            if side < 0:
                return False
        return True

    def get_sides(self) -> list[int]:
        return self.__sides

    def set_sides(self, *new_sides) -> None:
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)

    def __len__(self) -> int:
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color: tuple[int], *sides: int, filled: bool = True):
        super().__init__(color, sides, filled=filled)

        self.radius = len(self) / (2 * pi)

    def get_square(self) -> float:
        return pi * (self.radius**2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color: tuple[int], *sides: int, filled: bool = True):
        super().__init__(color, sides, filled=filled)

    def get_square(self) -> float:
        semiperimeter = sum(self.__sides) / 2

        return sqrt(
            semiperimeter
            * (semiperimeter - self.__sides[0])
            * (semiperimeter - self.__sides[1])
            * (semiperimeter - self.__sides[2])
        )


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: tuple[int], *sides: int, filled: bool = True):
        super().__init__(color, sides, filled=filled)
        self.__sides = [*sides] * 12

    def get_volume(self) -> float:
        return self.__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Color, sides)
cube1 = Cube((222, 35, 130), 6)

# Check for color changes:
circle1.set_color(55, 66, 77)  # Will change
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Will not change
print(cube1.get_color())

# Check for side changes:
cube1.set_sides(5, 3, 12, 4, 5)  # Will not change
print(cube1.get_sides())
circle1.set_sides(15)  # Will change
print(circle1.get_sides())

# Checking the perimeter (circle), this is the length:
print(len(circle1))

# Volume check (cube):
print(cube1.get_volume())


