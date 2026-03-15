import week_9_mod as mod


def main()-> None:
    """Main function to run code."""

    stack: mod.Stack = mod.Stack()
    queue: mod.Queue = mod.Queue()

    # print(stack)
    # stack.push(3)
    # stack.push(7)
    # stack.push(9)
    # stack.push(-1)
    # stack.push(100)
    # print(stack)

    # value: int = stack.pop()
    # print(value)
    # print(stack)
    # print(stack.pop())
    # print(stack)

    # print(stack.peek())
    # print(stack)

    print(queue)
    queue.add(10)
    queue.add(20)
    queue.add(30)
    print(queue)
    print(queue.remove())
    print(queue)
    print(queue.peek())
    print(queue)
    queue.add(35)
    queue.add(45)
    print(queue)


if __name__ == "__main__":
    main()