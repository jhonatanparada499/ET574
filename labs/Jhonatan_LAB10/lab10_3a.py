# lab10_3a.py - Jhonatan Parada

from math import pi
from lab10_2 import Rectangle

class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    def display(self):
        print('Radius:',self.radius)

    def setRadius(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius
    
    def area(self):
        return pi * (self.radius**2)
    
    def circumference(self):
        return 2 * pi * self.radius

def main():
    r = Rectangle()
    s = Circle(0)

    r.display()
    r.setWidth(1.25)
    r.setHeight(1.25)

    print('Get Width:',r.getWidth())
    print('Get Height:',r.getHeight())
    print(f'Area: {r.area():.5f}')
    print()

    s.display()
    s.setRadius(10)

    print('Get Radius:', s.getRadius())
    print(f'Area: {s.area():.5f}')
    print(f'Circumference: {s.circumference():.5f}')

if __name__ == '__main__': main()