import turtle

def draw_sqr(some,length):
    for j in range(0,100):
        for i in range(0,4):
            some.forward(length)
            some.right(90)
        some.right(5)
        limit =+ 1

    turtle.exitonclick()
    


def draw_art(length):
    window = turtle.Screen()
    window.bgcolor("red")

    sqr = turtle.Turtle()
    sqr.shape("turtle")
    sqr.color("yellow")
    sqr.speed(100)
    length_1 = int(length)
    
    draw_sqr(sqr, length_1)

    

length = raw_input("How long square do you wish for? Enter its side.")
draw_art(length)


    
    
