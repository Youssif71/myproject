from shape import Shape

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def draw(self):
        print(f"Drawing a {self.name} with radius {self.radius}")
