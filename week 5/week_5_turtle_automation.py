import turtle as tg
import csv


def main(): 
    """Turtle Automation by Riley Tuttle"""

    t: tg.Turtle = tg.Turtle()
    s: tg._Screen = tg.Screen()

    #Your Code here
    # Read commands from a file using with open() and csv.reader() or csv.DictReader.
    # Process the method commands using a conditional (if..elif..else) as you see fit
    # Supported commands: bgcolor, color, forward, backward, right, left
    # output "unknown command!" if the command is not in the above list.
    # Provide a general explanation of how your code works in a comment above this block of code

    # I used the with open to safely close the file and csv dict reader to open and then
    # used a for loop to dictread through each row in the csv file where I 
    # set the column headers "method" and "value" as keys for the csv dictionary and then set the 
    # method and value to two variables to be able to see if the value of the each column matches 
    # the values or commands that we are looking for with colors and directions
    # then i use a series of if else statements for each row to check what command is in the row and set the command to the value in the next column inside of the 
    # if statement where I also translate the values for the directions into a float so that the turtle module can interpret the read in values
    with open("moves.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Get the command and value from the dictionary
            command = row['method']
            value = row['value']

            if command == "bgcolor": 
                s.bgcolor(value)
            elif command == "color":
                t.color(value)
            elif command == "forward":
                t.forward(float(value))
            elif command == "backward":
                t.backward(float(value))
            elif command == "right":
                t.right(float(value))
            elif command == "left":
                t.left(float(value))
            else: 
                print("Unknown command!")


    s.mainloop()


main()