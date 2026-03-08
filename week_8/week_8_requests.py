import turtle as tg
import re
import calendar as cal

import requests as req


def main() -> None:
    """Request program by Riley Tuttle"""

    url: str = "https://www.wikipedia.org/wiki/Python_(programming language)"
    headers: dict[str, str] = {"User-Agent": "rtuttle1@atu.edu"}

    response: req.Response = req.get(url, headers = headers)
    page_content: str = response.text

    months: dict[str, int] = count_months(page_content)

    scn: tg._Screen = tg.Screen()
    scn.title("Turtle Requests")
    scn.colormode(255)
    scn.bgcolor(0, 0, 0)

    # Draw bars
    draw_bars(months)
    
    scn.mainloop()


def draw_bars(months: dict[str, int]) -> None:
    """Draw bar graph for the freq of each month"""

    pos: list[int] = [-300, -200]
    color: list = [150, 100 , 180]
    font: tuple = ("Consolas", 20, "bold")

    for month, freq in months.items():
        distance: int = freq * 5
        month_letter: str = month[0]

        draw_bar(distance, pos, color, month_letter, font)
        update_pos(pos, 50, 0)
        update_color(color)


def update_color(color: list[int]) -> None:
    """Update the color for the next bar"""

    color[0] = (color[0] + 2) % 256
    color[1] = (color[1] + 10) % 256
    color[2] = (color[2] - 10) % 256


def update_pos(pos: list[int], x_offset: int, y_offset: int) -> None:
    """Update the position for the next bar."""

    pos[0] += x_offset
    pos[1] += y_offset


def draw_bar(
        distance: int,
        pos: list[int],
        color: list[int],
        letter: str,
        font: tuple, 
) -> None:
    """Draw a bar for a month."""

    pen: tg.Turtle = tg.Turtle()
    pen.color(color)
    pen.width(40)
    pen.teleport(pos[0], pos[1])
    pen.write(letter, font= font, align="center")
    pen.left(90)
    pen.teleport(pos[0], pos[1] + 50)
    pen.forward(distance)


def count_months(content: str) -> dict[str, int]:
    """Count the number of times each month appears in content"""

    months: dict[str, int] = {}
    
    # Logic for determining number of months
    for month_num in range(1, 13):
        month: str = cal.month_name[month_num]
        pattern: str = month
        month_freq: list[str] = re.findall(pattern, content)
        months[month] = len(month_freq)


    return months



main()