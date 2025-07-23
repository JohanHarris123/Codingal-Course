import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(2)
t.hideturtle()

# === START OVAL ===
t.penup()
t.goto(-50, 250)
t.setheading(0)
t.pendown()
for _ in range(2):
    t.circle(20, 90)
    t.circle(50, 90)
t.penup()
t.goto(0, 240)
t.write("START", align="center", font=("Arial", 12, "normal"))

# ↓ Arrow to INPUT
t.goto(0, 230)
t.setheading(-90)
t.pendown()
t.forward(30)
t.right(150)
t.forward(10)
t.backward(10)
t.left(300)
t.forward(10)
t.backward(10)

# === INPUT NUMBER Rectangle ===
t.penup()
t.goto(-70, 180)
t.setheading(0)
t.pendown()
for _ in range(2):
    t.forward(140)
    t.right(90)
    t.forward(40)
    t.right(90)
t.penup()
t.goto(0, 160)
t.write("INPUT NUMBER", align="center", font=("Arial", 12, "normal"))

# ↓ Arrow to CONDITION
t.goto(0, 140)
t.setheading(-90)
t.pendown()
t.forward(30)
t.right(150)
t.forward(10)
t.backward(10)
t.left(300)
t.forward(10)
t.backward(10)

# === CONDITION Diamond ===
t.penup()
t.goto(0, 90)
t.pendown()
t.goto(80, 50)
t.goto(0, 10)
t.goto(-80, 50)
t.goto(0, 90)
t.penup()
t.goto(0, 45)
t.write("Is number % 2 == 0?", align="center", font=("Arial", 10, "normal"))

# ← YES arrow to EVEN
t.goto(-80, 50)
t.setheading(180)
t.pendown()
t.forward(40)
t.right(150)
t.forward(10)
t.backward(10)
t.left(300)
t.forward(10)
t.backward(10)
t.penup()
t.goto(-100, 60)
t.write("YES", align="center", font=("Arial", 10, "normal"))

# EVEN Rectangle
t.goto(-180, 30)
t.setheading(0)
t.pendown()
for _ in range(2):
    t.forward(140)
    t.right(90)
    t.forward(40)
    t.right(90)
t.penup()
t.goto(-110, 10)
t.write("Number is EVEN", align="center", font=("Arial", 12, "normal"))

# →→ Arrow from EVEN to END
t.goto(-110, -10)
t.setheading(-90)
t.pendown()
t.goto(-110, -40)
t.goto(0, -40)

# → NO arrow to ODD
t.penup()
t.goto(80, 50)
t.setheading(0)
t.pendown()
t.forward(40)
t.right(150)
t.forward(10)
t.backward(10)
t.left(300)
t.forward(10)
t.backward(10)
t.penup()
t.goto(100, 60)
t.write("NO", align="center", font=("Arial", 10, "normal"))

# ODD Rectangle
t.goto(120, 30)
t.setheading(0)
t.pendown()
for _ in range(2):
    t.forward(140)
    t.right(90)
    t.forward(40)
    t.right(90)
t.penup()
t.goto(190, 10)
t.write("Number is ODD", align="center", font=("Arial", 12, "normal"))

# →→ Arrow from ODD to END
t.goto(190, -10)
t.setheading(-90)
t.pendown()
t.goto(190, -40)
t.goto(0, -40)

# === END OVAL ===
t.penup()
t.goto(-50, -60)
t.setheading(0)
t.pendown()
for _ in range(2):
    t.circle(20, 90)
    t.circle(50, 90)
t.penup()
t.goto(0, -70)
t.write("END", align="center", font=("Arial", 12, "normal"))

turtle.done()
