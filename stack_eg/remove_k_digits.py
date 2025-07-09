from stack import Stack


stack_obj = Stack()


def remove_k_digits(num_string, k):

    for _num in num_string:
        num = int(_num)

        if k > 0 and not stack_obj.is_empty() and stack_obj.peek() > num:
            k -= 1
            stack_obj.pop()

        stack_obj.push(num)

    result = []
    while not stack_obj.is_empty():
        result.append(stack_obj.pop())

    return result[::-1]


if __name__ == "__main__":
    print("OUT: ", remove_k_digits("1432219", k=3))
