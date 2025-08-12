import turtle as t

t.Screen().bgcolor("orange")
b = t.Turtle()
b.speed(0)
b.width(2)

# Colors for the 6 triangles
colors = ["red", "green", "yellow", "purple", "cyan", "magenta"]

# Function to draw a filled triangle given starting position and heading
def draw_triangle(x, y, heading, color):
    b.penup()
    b.goto(x, y)
    b.setheading(heading)
    b.pendown()
    b.fillcolor(color)
    b.begin_fill()
    for _ in range(3):
        b.forward(100)
        b.left(120)
    b.end_fill()

# Draw the 6-pointed star (Star of David) and fill each outer triangle with a different color

import math

def star_point_coords(center_x, center_y, radius, angle_deg):
    angle_rad = math.radians(angle_deg)
    x = center_x + radius * math.cos(angle_rad)
    y = center_y + radius * math.sin(angle_rad)
    return x, y

center_x, center_y = 0, 0
outer_radius = 100
inner_radius = outer_radius * math.cos(math.radians(30))

# Get the 6 outer points of the star
points = [star_point_coords(center_x, center_y, outer_radius, 60 * i - 90) for i in range(6)]
# Get the 6 inner points (intersection points)
inner_points = [star_point_coords(center_x, center_y, inner_radius, 60 * i - 60) for i in range(6)]

# Draw and fill each of the 6 outer triangles
for i in range(6):
    b.penup()
    b.goto(center_x, center_y)
    b.pendown()
    b.fillcolor(colors[i])
    b.begin_fill()
    b.goto(points[i][0], points[i][1])
    b.goto(inner_points[i][0], inner_points[i][1])
    b.goto(points[(i+1)%6][0], points[(i+1)%6][1])
    b.goto(center_x, center_y)
    b.end_fill()

# Draw the two large triangles for the star outline
b.penup()
b.goto(points[0][0], points[0][1])
b.pendown()
b.pencolor("black")
for i in range(1, 7):
    b.goto(points[i % 6][0], points[i % 6][1])

b.penup()
b.goto(points[3][0], points[3][1])
b.pendown()
for i in range(1, 7):
    b.goto(points[(3 - i) % 6][0], points[(3 - i) % 6][1])

b.hideturtle()
t.done()