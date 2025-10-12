from shape import Shape 

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height
    
    def draw(self):
        print(f"Drawing a {self.name} with base {self.base} and height {self.height}")
