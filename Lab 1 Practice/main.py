from shape import Shape
from circle import Circle
from rectangle import Rectangle     
from triangle import Triangle

def main():
    shape = Shape("Generic Shape")
    shape.draw()
    
    circle = Circle(5)
    circle.draw()
    
    rect = Rectangle(4, 6)
    rect.draw()

    triangle = Triangle(3, 5)
    triangle.draw()

if __name__ == "__main__":
    main()