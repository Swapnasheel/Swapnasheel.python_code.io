import turtle

def draw_shape():
    window = turtle.Screen()
    window.bgcolor("blue")

    flower = turtle.Turtle()
    flower.speed(100)
    #flower.color("red")
    flower.shape("arrow")

    flower.right(45)

    for i in range(1,40):
        for j in range(1,5):
            draw_circle(flower, i, "red")
            flower.left(90)
    flower.right(45)
    flower.color("red")
    flower.forward(200)

    window.exitonclick()


def draw_circle(circle, radius, color):
    circle.color(color)
    circle.circle(radius)


draw_shape()
