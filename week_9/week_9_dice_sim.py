import pygal as pg
from pygal.style import Style

from week_9_dice import Die


def main() -> None:
    """Dice simulation program by Riley Tuttle."""

    # Create the dice
    die_one: Die = Die(20)
    die_two: Die = Die(20)

    # Simulate rolling the dices n times
    number_of_rolls: int = 1000

    results: list[int] = []

    for roll in range(number_of_rolls):
        result: int = die_one.roll() + die_two.roll()
        results.append(result)

    # Analyze the results
    counts: dict[int] = {}
    max_result: int = die_one.number_of_sides + die_two.number_of_sides

    for sum_value in range(2, max_result + 1):
        counts[sum_value] = results.count(sum_value)

    # Graph the results
    graph_style: Style = Style(
        colors = ("yellow", ),
        background = "gray",
        plot_background = "gray",
        foreground = "black",
        foreground_strong = "black",
        guide_stroke_color = "white",
        major_guide_stroke_color = "red",
    )

    graph: pg.Bar = pg.Bar(style=graph_style)
    graph.title = "Dice Roll Simulation by Riley Tuttle"

    graph.x_labels = counts.keys()
    graph.x_title = "Results"

    graph.add("Count", counts.values())
    graph.y_title = "Frequency"

    graph.render_to_file("dice_sim.svg")


if __name__ == "__main__":
    main()