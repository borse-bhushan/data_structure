from stack import Stack
from infix_to_postfix import infix_to_postfix

stack_obj = Stack()


def revers_infix(expression: list[str]):

    expression = expression[::-1]

    result = []
    for ch in expression:

        if ch.isalnum():
            result.append(ch)

        elif ch == "(":
            result.append(")")

        elif ch == ")":
            result.append("(")
        else:
            result.append(ch)

    return "".join(result)


def infix_to_prefix(expression: str):

    postfix = infix_to_postfix(revers_infix(expression))

    return postfix[::-1]


if __name__ == "__main__":
    print("OUT: ", infix_to_prefix(expression="(A+B)*C"))
