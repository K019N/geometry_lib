import math

from .shape import IShape


class Circle(IShape):
    def __init__(self, radius):
        if type(radius) not in [int, float]:
            raise TypeError("Радиус должен быть числом.")
        elif radius < 0:
            raise ValueError("Радиус треугольника не может быть отрицательным.")
        self.radius = radius
    
    @property
    def area(self):
        return math.pi * self.radius ** 2


class Triangle(IShape):
    def __init__(self, a, b, c):
        if any((type(a) not in [int, float], 
               type(b) not in [int, float],
               type(c) not in [int, float])):
            raise TypeError("Стороны фигуры должны быть числами.")
        elif any((a < 0, b < 0, c < 0)):
            raise ValueError("Сторона треугольника не может быть отрицательной.")
        elif any((a + b < c, a +c < b, c + b < a)):
            raise ValueError("Не существует треугольника с такими сторонами.")
        self.sides = [a, b, c]
        self.sides.sort()
        self.half_p = (a + b + c) / 2
        
    
    @property
    def area(self):
        if  self.sides[2] ** 2 == (self.sides[1] ** 2) + (self.sides[0] ** 2):
            return (self.sides[1] * self.sides[0]) / 2
        return (self.half_p * (self.half_p  - self.sides[0]) * 
                              (self.half_p  - self.sides[1]) * 
                              (self.half_p  - self.sides[2])) ** 0.5
