class Shape:
    def __init__(self, c):
        self.color = c

    def get_color(self):
        return self.color

    def get_area(self):
        pass  # Abstract method simulated in standard class

class Square(Shape):
    def __init__(self, c, side):
        super().__init__(c)
        self.side = side

    def get_area(self):
        return self.side * self.side

sq = Square("Red", 4)
print(sq.get_color())
print(sq.get_area())