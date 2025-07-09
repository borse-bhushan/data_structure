from stack import Stack

stack_obj = Stack()


def is_number(token):
    try:
        int(token)
        return True
    except ValueError:
        return False


def eval_postfix(tokens: list[str]):

    for token in tokens:

        if is_number(token):
            stack_obj.push(int(token))

        else:
            first_op = stack_obj.pop()
            second_op = stack_obj.pop()

            if token == "*":
                stack_obj.push(first_op * second_op)

            if token == "/":
                stack_obj.push(first_op / second_op)

            if token == "+":
                stack_obj.push(first_op + second_op)

            if token == "-":
                stack_obj.push(first_op - second_op)
    return stack_obj.pop()


if __name__ == "__main__":
    print("OUT: ", eval_postfix(tokens=["2", "3", "+", "4", "*"]))

    print("OUT: ", eval_postfix(tokens=["12", "-5", "*", "6", "+"]))
