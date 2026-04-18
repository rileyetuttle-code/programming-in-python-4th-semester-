from typing import Any


class Base: 
    """Base class for the Stack and Queue."""

    def __init__(self, structure_type: str) -> None:
        """Base initialize structure instance variables."""

        self.items: list[Any] = []
        self.structure_type: str = structure_type

    def __str__(self) -> str:
        """Return string for printing."""

        return f"{self.structure_type} Values: {self.items}"
        
    def is_empty(self) -> bool:
        """Return True if stucture is empty, False otherwise."""

        return len(self.items) <= 0
    
    def enter_item(self, item: int) -> None:
        """Add a value to the end of the structure."""

        self.items.append(item)



class Stack(Base): 
    """Stack class with a list."""

    def __init__(self) -> None: 
        """Initialize stack instance variables."""

        super().__init__("Stack")
    
    def get_value(self) -> int:
        """Remove and return the top (last) value in the stack."""

        if self.is_empty():
            return None

        return self.items.pop()

    def view_next(self) -> int:
        """Return the top (last) value in the stack."""

        if self.is_empty():
            return None

        return self.items[-1]


class Queue(Base): 
    """Queue class with a list."""

    def __init__(self) -> None: 
        """Initialize Queue instance variables."""

        super().__init__("Queue")
    
    def get_value(self) -> int:
        """Remove and return the first value in the queue."""

        if self.is_empty():
            return None

        return self.items.pop(0)

    def view_next(self) -> int:
        """Return the last value in the queue."""

        if self.is_empty():
            return None

        return self.items[0]


if __name__ == "__main__":
    print("This is a module...")
    b = Stack()
    print(b)
    b.enter_item(1)
    b.enter_item(2)
    print(b)
    print(b.view_next())
    print(b)