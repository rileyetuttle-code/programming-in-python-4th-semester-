import turtle as tg
import random as rm


def main():
    """Dots Program by Riley Tuttle."""

    t: tg.Turtle = tg.Turtle()
    s: tg._Screen = tg.Screen()

    s.bgcolor("black")
    t.speed(10)
    
    colors: list[str] = ["yellow", "blue", "hotpink", "green", "purple", "white", "red", "cyan", "orange"]

    count: int = 0
    total_dots: int = 500

    while count < total_dots:
        # generate x, y and size
        x: int = rm.randint(-400, 400)
        y: int = rm.randint(-400, 400)
        size: int = rm.randint(10, 75)

        # move the turtle
        t.teleport(x,y)

        # check x position and set color

        # my approach was to go through each of the 9 sections bottom up, then across. 
        # so my first 3 conditionals keep the x the same but change the y as it goes up 
        # the grid, then i move to the middle for the next 3 and go up, then the final 
        # column, with the last and top right grid just getting the else conditional
        color: str = "black"
        if x < -200 and y < -200:
            color = colors[0]
        elif x < -200 and y < 200:
            color = colors[1]
        elif x < -200:
            color = colors[2]
        elif x < 200 and y < -200:
            color = colors[3]
        elif x < 200 and y < 200:
            color = colors[4]
        elif x < 200:
            color = colors[5]
        elif x < 400 and y < -200:
            color = colors[6]
        elif x < 400 and y < 200:
            color = colors[7]
        else: 
            color = colors[8]


        # draw dot
        t.dot(size, color)

        # increment count
        count += 1

    s.mainloop()


main()