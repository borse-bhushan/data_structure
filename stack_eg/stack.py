class Stack:

    def __init__(self):

        self.stack = []

    def __str__(self):
        return "[" + ", ".join(self.stack) + "]"

    def push(self, item):
        self.stack.append(item)

        return True

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return False

    def is_empty(self):
        return not bool(self.stack)

    def size(self):
        return len(self.stack)

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return False


if __name__ == "__main__":
    stack = Stack()

    print(stack.is_empty())

    stack.push("HELLO")
    stack.push("WORD")
    stack.push("KKK")

    print(stack.is_empty())

    print(stack.pop())
    print(stack.peek())
    print(stack)
