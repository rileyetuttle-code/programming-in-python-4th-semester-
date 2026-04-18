class Stack:
    """Stack class: LIFO data structure."""

    def __init__(self) -> None:
        """Initialize stack instance variables."""

        self.values: list[int] = []

    def __str__(self) -> str:
        """Return string for printing."""

        return f"Stack Values: {self.values}"
    
    def push(self, value: int) -> None:
        """Add a value to the top (end) of the stack."""

        self.values.append(value)

    def pop(self) -> int:
        """Remove and return the top (last) value in the stack."""

        if self.is_empty():
            return None

        return self.values.pop()

    def peek(self) -> int:
        """Return the top (last) value in the stack."""

        if self.is_empty():
            return None

        return self.values[-1]
    
    def is_empty(self) -> bool:
        """Return True if stack is empty, False otherwise."""

        return len(self.values) <= 0
    

class Queue:
    """Queue class: FIFO data structure."""

    def __init__(self) -> None:
        """Initialize queue instance variables."""

        self.values: list[int] = []

    def __str__(self) -> str:
        """Return string for printing."""

        return f"Queue Values: {self.values}"
    
    def add(self, value: int) -> None:
        """Add a value to the back (end) of the queue."""

        self.values.append(value)

    def remove(self) -> int:
        """Remove and return the front (first) value in the queue."""

        if self.is_empty():
            return None

        return self.values.pop(0)

    def peek(self) -> int:
        """Return the front (first) value in the queue."""

        if self.is_empty():
            return None

        return self.values[0]
    
    def is_empty(self) -> bool:
        """Return True if queue is empty, False otherwise."""

        return len(self.values) <= 0


if __name__ == "__main__":
    print("This is a module...")