import turtle as tg
import random as rm


def main() -> None: 
    """Random Polygon application by Riley Tuttle"""

    # Variables
    number_of_shapes: int = 20
    max_sides: int = 6
    window_size: int = 200
    side_length_base: int = 300

    # Turtle setup
    t: tg.Turtle = tg.Turtle()
    s: tg._Screen = tg.Screen()

    s.bgcolor("black")
    t.speed(0)
    s.colormode(255)

    # Polygon Logic
    generate_shapes(
        number_of_shapes,
        window_size,
        max_sides,
        side_length_base,
        t,
    )
    
    # Keep loop going
    s.mainloop()


def generate_shapes(
    number_of_shapes: int,
    window_size: int,
    max_sides: int,
    side_length_base: int,
    t: tg.Turtle,
) -> None: 
    """Create random shapes using turtle graphics."""

    for _ in range(number_of_shapes):
        # Generate a random position
        pos: tuple[int] = (random_position(window_size))

        t.teleport(pos[0], pos[1])
        
        # Genereate a random color RGB
        t.color(random_color())

        # Generate a random number of sides
        num_sides: int = rm.randint(3, max_sides)
        angle: float = calculate_angle(num_sides)
        side_length: float = 100 / num_sides

        # Draw shape
        draw_shape(num_sides, side_length, angle, t)
        


def calculate_angle(sides: int) -> float:
    """Calculate the angle of a shape from the number of sides"""

    return 360 / sides


def random_position(window_size: int) -> tuple:
    """Use random library and window size as boundaries to create random values to store in a tuple for the turtle position"""
    x: int = rm.randint(-window_size, window_size)
    y: int = rm.randint(-window_size, window_size)
    pos: tuple[int] = (x,y)
    return pos


def random_color() -> tuple:
    """Generate random values for the RGB color to store in a color tuple"""

    r: int = rm.randint(0, 255)
    g: int = rm.randint(0, 255)
    b: int = rm.randint(0, 255)
    color: tuple[int] = (r, g, b)
    return color


def draw_shape(
    num_sides: int,
    side_length: int,
    angle: int,
    t: tg.Turtle,
) -> None:
    """Individual function with loop to draw each shape based on calculated values"""

    for side in range(num_sides): 
            t.forward(side_length)
            t.right(angle)


main()