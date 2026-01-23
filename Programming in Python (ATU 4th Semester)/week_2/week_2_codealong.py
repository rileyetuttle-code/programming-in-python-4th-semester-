import turtle as tg


def main(): 
    """Main part of the program."""

    # creating two turtles
    t1: tg.Turtle = tg.Turtle("turtle")
    t2: tg.Turtle = tg.Turtle("turtle")
    s: tg._Screen = tg.Screen()

    # screen settings
    s.colormode(255)
    s.bgcolor("black")

    # turtle settings
    t1.speed(4)
    t1.pensize(1)
    t2.speed(6)
    t2.pensize(2)

    # rgb color assignments
    r: int = 0
    g: int = 255
    b: int = 125

    # movement counts
    forwardCount: int = 15
    backwardCount: int = 10

    # loop condition assignments
    count: int = 0
    loops: int = 500

    # loop for turtle action
    while count < loops:
        # turtle 1 action
        t1.color(r, g, b)
        t1.forward(forwardCount)
        t1.right(91)

        # turtle 2 action
        t2.color("pink")
        t2.backward(backwardCount)
        t2.left(110)

        # counter and both RGB color changing
        count += 1
        forwardCount += 4
        backwardCount += 2
        r = (r + 1) % 256
        r = (g + 2) % 256
        r = (b - 20) % 256

        
    # TESTING GITHUB COMMIT
    

    s.mainloop()



main()


