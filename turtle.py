import turtle

class Polygon:
    def __init__(self, sides, name) -> None:
        self.sides = sides
        self.name = name 

    def draw(self):
        for i in range(self.sides):
            turtle.forward(100)
            turtle.right(90)
        turtle.done()
square = Polygon(4, "Square")
pentagon  = Polygon(5, "Pentagon")

print(square.sides)
print(square.name)

print(pentagon.name)
print(pentagon.sides)

