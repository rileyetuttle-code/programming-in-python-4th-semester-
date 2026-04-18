import tkinter as tk
from tkinter.font import Font

from week_11_mod import Stack, Queue
from week_11_helpers import Boxes, Box


def main() -> None:
    """Visual Stack and Queue program by Riley Tuttle."""

    # Create the window
    window: tk.Tk = tk.Tk()
    window.title("Stack and Queue Visual")
    font: Font = Font(family="Helvetica", size=20)

    # Frames for the left and right sides
    left: tk.Frame = tk.Frame(window, background="green")
    right: tk.Frame = tk.Frame(window, background="green")

    left.pack(side=tk.LEFT, expand=True, fill="both")
    right.pack(side=tk.RIGHT, expand=True, fill="both")

    # Stack section
    s_label: tk.Label = tk.Label(left, text="Stack", font=font, background="black", foreground="cyan")
    s_output: tk.Label = tk.Label(left, text="-", font=font, background="black", foreground="cyan")
    s_entry: tk.Entry = tk.Entry(left, font=font, background="black", foreground="cyan")

    s: Stack = Stack()
    s_box_section: tk.Frame = tk.Frame(left)
    s_boxes: Boxes = Boxes(s, s_box_section, font, s_output, s_entry)

    s_buttons: tk.Frame = tk.Frame(left)
    s_push: tk.Button = tk.Button(s_buttons, text="Push", font=font, command=s_boxes.add_box)
    s_pop: tk.Button = tk.Button(s_buttons, text="Pop", font=font, command=s_boxes.get_box)
    s_peek: tk.Button = tk.Button(s_buttons, text="Peek", font=font, command=s_boxes.peek_box)

    s_label.pack()
    s_output.pack()
    s_entry.pack()

    s_buttons.pack()
    s_push.pack(side=tk.LEFT)
    s_pop.pack(side=tk.LEFT)
    s_peek.pack(side=tk.LEFT)
    s_box_section.pack()

    # Queue Section
    q_label: tk.Label = tk.Label(right, text="Queue", font=font, background="black", foreground="cyan")
    q_output: tk.Label = tk.Label(right, text="-", font=font, background="black", foreground="cyan")
    q_entry: tk.Entry = tk.Entry(right, font=font, background="black", foreground="cyan")

    q: Queue = Queue()
    q_box_section: tk.Frame = tk.Frame(right)
    q_boxes: Boxes = Boxes(q, q_box_section, font, q_output, q_entry)

    q_buttons: tk.Frame = tk.Frame(right)
    q_add: tk.Button = tk.Button(q_buttons, text="Add", font=font, command=q_boxes.add_box)
    q_remove: tk.Button = tk.Button(q_buttons, text="Remove", font=font, command=q_boxes.get_box)
    q_peek: tk.Button = tk.Button(q_buttons, text="Peek", font=font, command=q_boxes.peek_box)

    q_label.pack()
    q_output.pack()
    q_entry.pack()

    q_buttons.pack()
    q_add.pack(side=tk.LEFT)
    q_remove.pack(side=tk.LEFT)
    q_peek.pack(side=tk.LEFT)
    q_box_section.pack()

    # Window
    window.mainloop()


if __name__ == "__main__":
    main()