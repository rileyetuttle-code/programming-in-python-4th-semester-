import tkinter as tk
import random as rm
import time as tm


def main():
    """Visual Sort 2.0 application by Riley TUttle."""

    # Variables
    num_of_bars: int = 20
    speed: float = .1
    max_height: int = 500
    width: int = 20

    y_pad: int = 1
    x_pad: int = 1

    colors: dict[str, str] = {
        "background":"black",
        "unsorted":"white",
        "sorted":"dark blue",
        "highlight":"orange",
        "best": "hot pink"
    }

    # Window setup
    wn: tk.Tk = tk.Tk()
    wn.title("Visual Sort")
    wn.config(bg=colors["background"])

    # Create random bars
    bars: list[tk.frame] = create_bars(num_of_bars, max_height, wn, colors, width, x_pad, y_pad)

    # Selection Sort
    selection_sort(bars, colors, x_pad, y_pad, wn, speed)

    # Bubble Sort
    bubble_sort(bars, colors, x_pad, y_pad, wn, speed)

    # Insertion Sort
    insertion_sort(bars, colors, x_pad, y_pad, wn, speed)

    # Keep window open
    wn.mainloop()


# Sorting Functions


# Bubble Sort
def bubble_sort(
    bars: list[tk.Frame],
    colors: dict[str, str],
    x_pad: int,
    y_pad: int,
    wn: tk.Tk,
    speed: float
) -> None:
    """bubble sort on bars by comparing each bar starting from the left to its neighbor on the right and swapping
    them if the left is bigger than the right continuously until the bar finds a bar it is smaller than and stops,
    eventually creating an organized and in order list of bars"""

    for next_pos in range(len(bars)):
        for current_pos in range(len(bars)-1-next_pos):

            if bars[current_pos].winfo_reqheight() > bars[current_pos+1].winfo_reqheight():
                swap_bars(bars, current_pos, current_pos + 1)

            bars[current_pos+1].config(bg=colors["highlight"])
            bars[current_pos].config(bg=colors["unsorted"])
            update_bars(bars, x_pad, y_pad, wn, speed)

        bars[-next_pos-1].config(bg=colors["sorted"])


# Insertion Sort
def insertion_sort(
    bars: list[tk.Frame], 
    colors: dict[str, str],
    x_pad: int,
    y_pad: int,
    wn: tk.Tk,
    speed: float
) -> None:
    """Perform an insertion sort on bars by comparing bars to their adjacent left bar and swapping them 
    if it is smaller to create an organized, in order set of bars from the left first"""

    bars[0].config(bg=colors["sorted"]) # Assume the first bar is sorted

    for next_unsorted in range(1, len(bars)):
        bars[next_unsorted].config(bg=colors["highlight"]) # Highlight the bar that is being moved
       
        current_pos: int = next_unsorted - 1

        while current_pos >= 0 and bars[current_pos].winfo_reqheight() > bars[current_pos+1].winfo_reqheight():
            swap_bars(bars, current_pos, current_pos + 1)
            current_pos -= 1
            update_bars(bars, x_pad, y_pad, wn, speed)

        bars[current_pos+1].config(bg=colors["sorted"]) # Color the sorted bar when it is in the right place


# Selection Sort
def selection_sort(
    bars: list[tk.Frame], 
    colors: dict[str, str],
    x_pad: int,
    y_pad: int,
    wn: tk.Tk,
    speed: float,
) -> None: 
    """Perform a selection sort on bars. A selection sort
    sorts by repeatedly finding the minimum element from
    the unsorted part and putting it at the next unsorted position"""

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
    """Swap the left bar with the right bar in the bar list"""

    bars[left], bars[right] = bars[right], bars[left]


def set_color(bar: tk.Frame, color: str) -> None:
    """Set the color of the bar"""

    bar.config(bg=color)


def create_bars(
        num_of_bars: int, 
        max_height: int, 
        wn: tk.Tk, 
        colors: list[str, str], 
        width: int, 
        x_pad: int, 
        y_pad: int) -> list:
        """Intial creation of the bars using created bar restraints like width and max height,
        but randomizing the height of each one and packing them together to create the random unsorted
        bars we initially see on screen"""

        bars: list[tk.Frame] = []
        for _ in range(num_of_bars):
            height: int = rm.randint(1, max_height)
            bar: tk.Frame = tk.Frame(
                wn, height=height, width=width, bg=colors["unsorted"]
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