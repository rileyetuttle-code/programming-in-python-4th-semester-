import tkinter as tk
import random as rm
import time as tm


def main():
    """Visual Sort application by Riley Tuttle"""

    # Variables
    num_of_bars: int = 20
    speed: float = .1
    max_height: int = 500
    width: int = 20

    y_pad: int = 1
    x_pad: int = 1

    colors: dict[str, str] = {
        "background":"black",
        "unsorted": "white",
        "sorted": "hotpink",
        "highlight": "red",
    }

    # Window Setup
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

    # Bubble sort
    # bubble sort works by starting from the very left and comparing the first value to the second value
    # and determing which is bigger. if the first bar is taller, it swaps the first and second bar and now
    # the new second bar ( the original first bar ) is being compared to the third bar, and so on until the 
    # current bar finds a taller bar infront of it and then the sorting goes to the beginnnig and does the same
    # process over again by moving the bars down the line until they find a bar bigger then them and are all in order
    # for i in range(len(bars)):
    #     for j in range(len(bars)-1-i):
    #         if bars[j].winfo_reqheight() > bars[j + 1].winfo_reqheight():
    #             bars[j], bars[j + 1] = bars[j + 1], bars[j]
    #         bars[j + 1].config(bg=colors["highlight"])
    #         bars[j].config(bg=colors["unsorted"])
    #         update_bars(bars, x_pad, y_pad, wn, speed)
    #     bars[-i-1].config(bg=colors["sorted"])
        
    # Insertion Sort
    # insertion sort starts from the left side and "highlights" or selects its first bar and compares it
    # to the bar on its left to see if the bar on the left is > the highlighted bar, if it is, it swaps them 
    # and continues this trend until the bar on the left is no longer bigger and is in order. My colors worked
    # by using the highlight color on the k + 1 bar or inserted bar being worked on in the while loop
    # then updating the bars. next, after performing the swap, i made the k + 1 bar the sorted color because it is in the correct
    # order after being swapped and then once once getting out of the loop for that k + 1 it gets the sorted color
    # because it is in its final position and therefore in order and updated
    bars[0].config(bg=colors["sorted"])  # Mark first bar as sorted
    for j in range(1, len(bars)):
        k: int = j - 1
        while k >= 0 and bars[k].winfo_reqheight() > bars[k + 1].winfo_reqheight():
            bars[k + 1].config(bg=colors["highlight"])
            update_bars(bars, x_pad, y_pad, wn, speed)
            
            bars[k], bars[k + 1] = bars[k + 1], bars[k]
            bars[k + 1].config(bg=colors["sorted"])
            k -= 1
        
        bars[k + 1].config(bg=colors["sorted"])
        update_bars(bars, x_pad, y_pad, wn, speed)
        

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
    """This function packs the bars in the list and then unpacks them again in the new ordered position
    to display their updated position after swaps"""

    for bar in bars:
        bar.pack_forget()
    for bar in bars:
        bar.pack(side="left", anchor="s", pady=y_pad, padx=x_pad)
    wn.update()
    tm.sleep(speed)


main()