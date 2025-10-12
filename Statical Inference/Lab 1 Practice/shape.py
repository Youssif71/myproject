class Shape:
    def __init__(self, name):
        self.name = name
    
    def draw(self):
        print(f"Drawing a shape: {self.name}")