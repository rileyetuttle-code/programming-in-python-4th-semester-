import tkinter as tk
import random as rm
import time as tm


def main():
    """Visual Sort application by NAME_HERE."""

    # Variables
    num_of_bars: int = 20
    speed: float = .1
    max_height: int = 500
    width: int = 20

    y_pad: int = 1
    x_pad: int = 1

    colors: dict[str, str] = {
        "background":"black",
        "unsorted":"gray",
        "sorted":"limegreen",
        "highlight":"yellow",
    }

    # Window setup
    wn: tk.Tk = tk.Tk()
    wn.title("Visual Sort")
    wn.config(bg=colors["background"])

    # Create random bars
    bars: list[tk.Frame] = []
    for _ in range(num_of_bars):
        height: int = rm.randint(1, max_height)
        bar: tk.Frame = tk.Frame(
            wn, height=height, width=width, bg=colors["unsorted"]
        )
        bar.pack(side="left", anchor="s", pady=y_pad, padx=x_pad)
        bars.append(bar)

    # Bubble Sort
    # for i in range(len(bars)):
    #     for j in range(len(bars)-1-i):
    #         if bars[j].winfo_reqheight() > bars[j+1].winfo_reqheight():
    #             bars[j], bars[j+1] = bars[j+1], bars[j]
    #         bars[j+1].config(bg=colors["highlight"])
    #         bars[j].config(bg=colors["unsorted"])
    #         update_bars(bars, x_pad, y_pad, wn, speed)
    #     bars[-i-1].config(bg=colors["sorted"])

    # Insertion Sort
    bars[0].config(bg=colors["sorted"]) # Assume the first bar is sorted
    for j in range(1, len(bars)):
        bars[j].config(bg=colors["highlight"]) # Highlight the bar that is being moved
        k: int = j - 1
        while k >= 0 and bars[k].winfo_reqheight() > bars[k+1].winfo_reqheight():
            bars[k], bars[k+1] = bars[k+1], bars[k]
            k -= 1
            update_bars(bars, x_pad, y_pad, wn, speed)
        bars[k+1].config(bg=colors["sorted"]) # Color the sorted bar when it is in the right place

    # Keep window open
    wn.mainloop()


# Section for updating the bars
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