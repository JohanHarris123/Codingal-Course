import turtle

sc = turtle.Screen()
# creating canvas
sc.bgcolor("pink")

sc.setup(700, 700)

sc.title("Welcome to Turtle.Window")

# turtle object creation
board = turtle.Turtle()

n = 6
# creating a square
board.fillcolor('violet')
board.begin_fill()
for i in range(n):
    board.forward(100)
    board.left(360/n)
board.end_fill()

lst = ['orange', 'red', 'green', 'yellow', 'blue', 'brown']
for i in range(len(lst)):
    board.fillcolor(lst[i])
    board.begin_fill()
    board.right(60)
    board.forward(100)
    board.left(120)
    board.forward(100)
    board.end_fill()

turtle.done()