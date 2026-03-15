import tkinter as tk
import random as rm
import time as tm


def main():
    """Visual Sort 2.0 application by NAME_HERE."""

    # Variables
    num_of_bars: int = 30
    speed: float = .01
    max_height: int = 500
    width: int = 20

    y_pad: int = 1
    x_pad: int = 1

    colors: dict[str, str] = {
        "background":"black",
        "unsorted":"gray",
        "sorted":"limegreen",
        "highlight":"yellow",
        "best": "red",
    }

    # Window setup
    wn: tk.Tk = tk.Tk()
    wn.title("Visual Sort")
    wn.config(bg=colors["background"])

    # Create random bars
    bars: list[tk.Frame] = create_bars(
        wn,
        num_of_bars,
        max_height,
        width,
        colors,
        x_pad,
        y_pad,
    )

    # Sorts
    # Selection Sort
    # selection_sort(bars, colors, x_pad, y_pad, wn, speed)
    
    # Bubble Sort
    # bubble_sort(bars, colors, x_pad, y_pad, wn, speed)

    # Insertion Sort
    insertion_sort(bars, colors, x_pad, y_pad, wn, speed)

    # Keep window open
    wn.mainloop()


# Sort Functions
def bubble_sort(
    bars: list[tk.Frame],
    colors: dict[str, str],
    x_pad: int,
    y_pad: int,
    wn: tk.Tk,
    speed: float,
) -> None:
    """Perform a bubble sort on bars. A bubble sort repeatedly steps through the list,
    compares adjacent elements and swaps them if they are in the wrong order. The pass through the
    list is repeated until the list is sorted.
    """

    for next_pos in range(len(bars)):
        for current_pos in range(len(bars)-1-next_pos):

            if bars[current_pos].winfo_reqheight() > bars[current_pos+1].winfo_reqheight():
                swap_bars(bars, current_pos, current_pos + 1)

            set_color(bars[current_pos+1], colors["highlight"])
            set_color(bars[current_pos], colors["unsorted"])
            update_bars(bars, x_pad, y_pad, wn, speed)

        set_color(bars[-next_pos - 1], colors["sorted"])
    update_bars(bars, x_pad, y_pad, wn, speed)


def insertion_sort(
    bars: list[tk.Frame],
    colors: dict[str, str],
    x_pad: int,
    y_pad: int,
    wn: tk.Tk,
    speed: float,
) -> None:
    """Perform an insertion sort on bars. An insertion sort builds the final sorted array one item at a time.
    It iterates through the list and removes one element, finds the location it belongs to in the sorted list
    and inserts it there. It repeats until no input elements remain.
    """

    set_color(bars[0], colors["sorted"]) # Assume the first bar is sorted
    for next_unsorted in range(1, len(bars)):

        set_color(bars[next_unsorted], colors["highlight"]) # Highlight the bar that is being moved
        current_pos: int = next_unsorted - 1

        while current_pos >= 0 and bars[current_pos].winfo_reqheight() > bars[current_pos+1].winfo_reqheight():
            swap_bars(bars, current_pos, current_pos + 1)
            current_pos -= 1
            update_bars(bars, x_pad, y_pad, wn, speed)

        set_color(bars[current_pos+1], colors["sorted"]) # Color the sorted bar when it is in the right place
    update_bars(bars, x_pad, y_pad, wn, speed)


def selection_sort(
    bars: list[tk.Frame],
    colors: dict[str, str],
    x_pad: int,
    y_pad: int,
    wn: tk.Tk,
    speed: float,
) -> None:
    """Peform a selection sort on bars. A selection sort
    sorts by repeatedly finding the minimum element from
    the unsorted part and putting it at the next unsorted position.
    """
    
    for next_spot in range(len(bars)):
        best_pos: int = next_spot
        set_color(bars[best_pos], colors["best"])

        for current_pos in range(next_spot + 1, len(bars)):
            set_color(bars[current_pos], colors["highlight"])
            update_bars(bars, x_pad, y_pad, wn, speed)

            if bars[current_pos].winfo_reqheight() < bars[best_pos].winfo_reqheight():
                set_color(bars[best_pos], colors["unsorted"])
                set_color(bars[current_pos], colors["best"])
                best_pos = current_pos
            else:
                set_color(bars[current_pos], colors["unsorted"])
                
        swap_bars(bars, next_spot, best_pos)
        set_color(bars[next_spot], colors["sorted"])
    update_bars(bars, x_pad, y_pad, wn, speed)


# Helper Functions
def swap_bars(bars: list[tk.Frame], left: int, right: int) -> None:
    """Swap the left bar with the right bar in the bars list."""

    bars[left], bars[right] = bars[right], bars[left]


def set_color(bar: tk.Frame, color: str) -> None:
    """Set the color of the bar."""

    bar.config(bg=color)


def create_bars(
    wn: tk.Tk,
    num_of_bars: int,
    max_height: int,
    width: int,
    colors: dict[str, str],
    x_pad: int,
    y_pad: int,
) -> list[tk.Frame]:
    """Create a list of bars with random heights."""
    
    bars: list[tk.Frame] = []

    for _ in range(num_of_bars):
        height: int = rm.randint(1, max_height)
        bar: tk.Frame = tk.Frame(
            wn,
            height=height,
            width=width,
            bg=colors["unsorted"],
        )
        bar.pack(side="left", anchor="s", pady=y_pad, padx=x_pad)
        bars.append(bar)

    return bars


def update_bars(
    bars: list[tk.Frame],
    x_pad: int,
    y_pad: int,
    wn: tk.Tk,
    speed: float,
) -> None:
    """Repack the bars and update the window to show changes."""

    for bar in bars:
        bar.pack_forget()
    for bar in bars:
        bar.pack(side="left", anchor="s", pady=y_pad, padx=x_pad)
    wn.update()
    tm.sleep(speed)


main()