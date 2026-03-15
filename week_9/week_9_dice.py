import random as rm


class Die: 
    """Die class with a number of sides and a roll method."""

    def __init__(self, number_of_sides: int) -> None:
        
        self.number_of_sides: int = number_of_sides

    def __str__(self) -> str:
        """String for printing."""

        return f"A {self.number_of_sides}-sided die."
    
    def roll(self) -> int:
        """Roll the die and return the result."""

        return rm.randint(1, self.number_of_sides)


if __name__ == "__main__":
    print("This is a module...")

    die1: Die = Die(6)
    print(die1.roll())

    print(die1)