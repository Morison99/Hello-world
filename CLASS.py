class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"point ({self.x},{self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.draw()

    def distance(self, x2, y2):

        X = (x2-self.x)**2
        Y = (y2-self.y)**2
        print(X)
        print(Y)
        D = (X+Y)**0.5
        print("distance is ", D)


point = Point(1, 2)
print(point.x)
print(point.y)
point.draw()
# point.move(1, 2)
point.distance(5, 6)
