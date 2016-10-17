import turtle


def draw_square(some_turtle):
    repeat = 0
    while repeat < 4:
        some_turtle.forward(100)
        some_turtle.right(90)
        repeat = repeat + 1

def draw_triangle(some_turtle):
    some_turtle.right(60)
    some_turtle.forward(100)
    some_turtle.right(60)
    some_turtle.forward(100)
    some_turtle.right(150)
    some_turtle.forward(160)
    
        

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    
    #Create the Square turtle
    sqr = turtle.Turtle()
    sqr.shape("turtle")
    sqr.color("blue")
    draw_square(sqr)
    
    #Draw Circle
    cir = turtle.Turtle()
    cir.shape("turtle")
    cir.color("yellow")
    cir.circle(50)

    #Draw Triangle
    tri = turtle.Turtle()
    tri.shape("arrow")
    tri.color("green")
    draw_triangle(tri)
    

    window.exitonclick()
    

draw_art()
