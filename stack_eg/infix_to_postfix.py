from stack import Stack


stack_obj = Stack()


def infix_to_postfix(expression: str):

    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
    results = []

    for ch in expression:

        if ch.isalnum():
            results.append(ch)

        elif ch == "(":
            stack_obj.push(ch)

        elif ch == ")":

            while not stack_obj.is_empty() and stack_obj.peek() != "(":
                results.append(stack_obj.pop())
            stack_obj.pop()

        else:
            while (
                not stack_obj.is_empty()
                and stack_obj.peek() != "("
                and precedence.get(ch, 0) <= precedence.get(stack_obj.peek(), 0)
            ):
                results.append(stack_obj.pop())
            stack_obj.push(ch)

    while not stack_obj.is_empty():
        results.append(stack_obj.pop())

    return "".join(results)


if __name__ == "__main__":
    print("OUT: ", infix_to_postfix(expression="(A+B)*C"))
