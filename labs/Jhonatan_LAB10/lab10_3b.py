# lab10_3b.py - Jhonatan Parada

from shapes import Rectangle, Circle

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