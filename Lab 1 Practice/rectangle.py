from shape import Shape

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def draw(self):
        print(f"Drawing a {self.name} with width {self.width} and height {self.height}")
