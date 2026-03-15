import tkinter as tk
import random as rm
import time as tm


def main() -> None: 
    """Visual Sort 3.0 application by Riley Tuttle."""

    # Variables
    num_of_bars: int = 30
    speed: float = .01
    max_bar_height: int = 500
    bar_width: int = 20

    bar_spacing: int = 1

    # Window Setup
    wn: tk.Tk = tk.Tk()
    wn.title("Visual Sort")
    wn.config(bg=Color.BACKGROUND)

    # Create Bars
    bars: Bars = Bars(wn, speed, bar_spacing)
    bars.create_bars(num_of_bars, max_bar_height, bar_width)

    # Sort Bars
    # bars.bubble_sort()

    # Insertion Sort
    # bars.insertion_sort()

    # Selection Sort
    bars.selection_sort()

    # Keep window open
    wn.mainloop()


class Bars: 
    """Bars class with a list of bar objects and methods to work on the bar objects."""

    def __init__(self, wn: tk, speed: float, spacing: int) -> None:
        """Create a new set of bars."""

        self.bars: list[Bar] = []
        self.wn: tk.Tk = wn
        self.speed: float = speed
        self.spacing: int = spacing

    def __str__(self) -> str:
        """Print friendly."""

        return f"Bars: {self.bars}"
    
    def create_bars(
        self,
        num_of_bars: int,
        max_height: int,
        width: int,
    ) -> None: 
        """Create a list of bar objects with random heights."""

        for _ in range(num_of_bars):
            height: int = rm.randint(1, max_height)
            bar: Bar = Bar(height, width, color=Color.UNSORTED, wn=self.wn)
            self.bars.append(bar)
        self.update_bars()

    def update_bars(self) -> None:
        """Update the display of th ebars by forgetting and repacking them."""

        for bar in self.bars:
            bar.frame.pack_forget()
        for bar in self.bars:
            bar.frame.pack(side=tk.LEFT, anchor=tk.S, pady=1, padx=self.spacing)
        self.wn.update()
        tm.sleep(self.speed)

    def swap_bars(self, left: int, right: int) -> None:
        """Swap the left bar with the right bar in the bars list."""

        self.bars[left], self.bars[right] = self.bars[right], self.bars[left]

    def bubble_sort(self) -> None:
        """Perform a bubble sort on bars. A bubble sort repeatedly steps through the list,
        compares adjacent elements and swaps them if they are in the wrong order. The pass through the
        list is repeated until the list is sorted.
        """

        for next_pos in range(len(self.bars)):
            for current_pos in range(len(self.bars)-1-next_pos):

                if self.bars[current_pos] > self.bars[current_pos+1]:
                    self.swap_bars(current_pos, current_pos + 1)

                self.bars[current_pos+1].color(Color.HIGHLIGHT)
                self.bars[current_pos].color(Color.UNSORTED)
                self.update_bars()

            self.bars[-next_pos - 1].color(Color.SORTED)
        self.update_bars()
    
    def insertion_sort(self) -> None:
        """Perform an insertion sort on bars. An insertion sort builds the final sorted array one item at a time.
        It iterates through the list and removes one element, finds the location it belongs to in the sorted list
        and inserts it there. It repeats until no input elements remain.
        """

        self.bars[0].color(Color.SORTED) # Assume the first bar is sorted (used 0 because current pos isn't defined yet and outsite of the loop we know the current pos is 0)
        for next_unsorted in range(1, len(self.bars)):
 
            self.bars[next_unsorted].color(Color.HIGHLIGHT) # Highlight the bar that is being moved
            current_pos: int = next_unsorted - 1

            while current_pos >= 0 and self.bars[current_pos] > self.bars[current_pos+1]:
                self.swap_bars(current_pos, current_pos + 1)
                current_pos -= 1
                self.update_bars()

            self.bars[current_pos+1].color(Color.SORTED)  # Color the sorted bar when it is in the right place
        self.update_bars()
    
    def selection_sort(self) -> None:
        """Peform a selection sort on bars. A selection sort
        sorts by repeatedly finding the minimum element from
        the unsorted part and putting it at the next unsorted position.
        """
        
        for next_spot in range(len(self.bars)):
            best_pos: int = next_spot
            self.bars[best_pos].color(Color.BEST)

            for current_pos in range(next_spot + 1, len(self.bars)):
                self.bars[current_pos].color(Color.HIGHLIGHT)
                self.update_bars()

                if self.bars[current_pos] < self.bars[best_pos]:
                    self.bars[best_pos].color(Color.UNSORTED)
                    self.bars[current_pos].color(Color.BEST)
                    best_pos = current_pos
                else:
                    self.bars[current_pos].color(Color.UNSORTED)
                    
            self.swap_bars(next_spot, best_pos)
            self.bars[next_spot].color(Color.SORTED)
        self.update_bars()

class Bar: 
    """Bar class with a height and color."""

    def __init__(self, height: int, width: int, color: str, wn: tk.Tk) -> None:
        """Create a bar."""

        self.height: int = height
        self.frame: tk.Frame = tk.Frame(wn, width=width, height=self.height, bg=color)

    def __gt__(self, other: Bar) -> bool:
        """Return true if greater than other bar, False otherwise."""

        return self.height > other.height
    
    def __ge__(self, other: Bar) -> bool:
        """Return true if greater than or equal to other bar, False otherwise."""

        return self.height >= other.height
    
    def __lt__(self, other: Bar) -> bool:
        """Return true if less than other bar, False otherwise."""

        return self.height < other.height
    
    def __le__(self, other: Bar) -> bool:
        """Return true if less than or equal to other bar, False otherwise."""

        return self.height <= other.height

    def __str__(self) -> str:
        """Bar String."""

        return f"Bar({self.height})"
    
    def __repr__(self) -> str:
        """Bar representation."""

        return f"Bar({self.height})"
    
    def color(self, color: str) -> None:
        """Change the color of the frame on the bar."""

        self.frame.config(bg=color)



class Color:
    """A class to store colors."""

    BACKGROUND: str = "dark gray"
    UNSORTED: str = "white"
    SORTED: str = "blue"
    HIGHLIGHT: str = "cyan"
    BEST: str = "orange"

if __name__ == "__main__":
    main()
