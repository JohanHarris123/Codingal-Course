import turtle as t
sc = t.Screen()
#creating canvas
sc.bgcolor("pink")

sc.setup(500,500)

t.title("Welcome to Turtle Window")

# turtle object creation
board = t.Turtle()

n=6
# creating a square
board.color("red")
board.width(10)
board.fillcolor("yellow")
board.begin_fill()
for i in range(n):
    board.forward(100)
    board.left(360/n)
board.end_fill()

t.done()