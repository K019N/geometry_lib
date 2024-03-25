from figures import *

#не особо понял что значит реализовать вычисление площади фигуры без знания типа фигуры в compile-time
#поэтому прибегнул к такой реализаци
def calc_area(shape):
    return shape.area

if __name__ == "__main__":
    circle = Circle(5)
    triangle = Triangle(3, 4, 5)
    print(calc_area(triangle))
    print(calc_area(circle))
