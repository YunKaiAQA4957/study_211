class Figure:
    def __init__(self, name):
        self.name = name
 
class Rectangle(Figure):
    def __init__(self, a, b):
        self.a, self.b = a, b
        super().__init__('прямоугольник')
 
    def __str__(self):
        return (f'Фигура: {self.name}; площадь: {self.a * self.b}')

    
class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
        super().__init__('круг')
 
    def __str__(self):
        return (f'Фигура: {self.name}; площадь: {3.14 * self.radius ** 2}')
 
class RightTriangle(Figure):
    def __init__(self, leg_1, leg_2):
        self.leg_1, self.leg_2 = leg_1, leg_2
        super().__init__('прямоугольный треугольник')
 
    def __str__(self):
        return (f'Фигура: {self.name}; площадь: {self.leg_1 * self.leg_2 / 2}')
    
class Trapezoid(Figure):
    def __init__(self, a, b, h):
        self.a, self.b, self.h = a, b, h
        super().__init__('трапеция')
 
    def __str__(self):
        return (f'Фигура: {self.name}; площадь: {((self.a + self.b) / 2) * self.h}')
 

r = Rectangle(25, 33)
print(r)
c = Circle(47)
print(c)
rt = RightTriangle(92, 44)
print(rt)
trapezoid = Trapezoid(51, 12, 26)
print(trapezoid)