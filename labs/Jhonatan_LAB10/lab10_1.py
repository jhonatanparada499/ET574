# lab10_1.py - Jhonatan Parada

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def display(self):
        print(
            f'Width: {self.width}\n'
            f'Height: {self.height}'
        )

def main():
    r1 = Rectangle(4, 5)
    r2 = Rectangle(10, 10)

    r1.display()
    r2.display()

    print(
        f'Width of r1: {r1.width}\n'
        f'Height of r2: {r2.height}'
    )

if __name__ == '__main__': main()