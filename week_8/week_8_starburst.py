import turtle as tg


def main() -> None: 
    """Starburst program by NAME."""

    # Change the colors
    colors: list[tuple] = [
        (0, 0, 255),
        (30, 15, 255),
        (70, 30, 255),
        (100, 45, 255),
        (130, 60, 255),
        (160, 75, 255),
        (190, 90, 255),
    ]

    symbols: list[str] = [
        "\u2745",
        "\u2746",
        "\u2747",
        "\u2748",
        "\u2749",
        "\u274A",
        "\u274B",
    ]

    pen: tg.Turtle = tg.Turtle()
    scn: tg._Screen = tg.Screen()

    pen.speed(0)
    pen.penup()
    scn.bgcolor("black")
    scn.colormode(255)

    # draw function
    draw_starburst(pen, symbols, colors)

    scn.mainloop()


def draw_starburst(
        pen: tg.Turtle,
        symbols: list, 
        colors: list ) -> None:
    """This function uses a loop and calculations for color and symbols to create a random series of symbols in a sprialling shape"""

    for i in range(2, 360):
        font_size: int = i // 2 
        font_style: tuple = ("Consolas", font_size, "normal")
        color: tuple[int] = colors[i % len(colors)]
        symbol: str = symbols[i % len(symbols)]

        pen.color(color)
        pen.forward(i * 2)
        pen.right(49)
        pen.write(symbol, font=font_style)


main()