# lab10_2.py - Jhonatan Parada

from lab10_1 import Rectangle as Parent_rectangle

# Rectangle is inheriting the methods from Parent_rectangle
class Rectangle(Parent_rectangle):
    def __init__(self, width=1, height=1):
        Parent_rectangle.__init__(self, width, height)

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
    def area(self):
        return self.width * self.height

def main():
    r1 = Rectangle(4, 5)
    r2 = Rectangle()

    r1.display()
    print('Area:',r1.area())

    r2.display()
    print('Area:',r2.area())

    r2.setWidth(6)
    r2.setHeight(6)

    print('Get Width:',r2.getWidth())
    print('Get Height',r2.getHeight())
    print('Area:',r2.area())

if __name__ == '__main__': main()