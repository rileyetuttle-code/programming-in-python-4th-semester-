import turtle as tg


def main():
    """Fibonacci Squares by Riley Tuttle"""

    colors: list[str] = ["hotpink", "cyan", "yellow", "purple"] # pick your own colors
    line_color: str = "white"
    total_squares: int = 14
    square_count: int = 0

    t: tg.Turtle = tg.Turtle()
    s: tg._Screen = tg.Screen()

    t.speed(0)
    s.bgcolor("black")

    a: int = 0
    b: int = 1
    c: int = 0

    while square_count < total_squares:
        # Calculating fib number
        c = a + b 
        # Preparing for next iteration
        a = b
        b = c

        # Draw the square
        t.color(line_color, colors[square_count % len(colors)])

        # my approach to filling the entire square was that the reason it was split in half was 
        # because it was refilling the 2 extra sides in the range of 6 back to black, so I needed
        # to stop the filling after it had done just 4 sides, so I put in a conditional statement
        # to detect when it had completed 4 sides in the for loop and to stop filling for that square
        t.begin_fill()
        for side in range(6):
            t.forward(c)
            t.right(90)
            if side == 4:
                t.end_fill()
        
        t.left(90)
        

        square_count += 1

    s.mainloop()


main()