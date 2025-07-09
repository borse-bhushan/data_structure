from stack import Stack


def next_greater_element(nums: list[int]):

    for index in range(0, len(nums)):
        is_changed = False
        for next_index in range(index, len(nums)):
            if nums[index] < nums[next_index]:
                nums[index] = nums[next_index]
                is_changed = True
                break

        if not is_changed:
            nums[index] = -1

    return nums


stack_obj = Stack()


def next_greater_element_using_stack(nums):

    result = []
    for num in nums[::-1]:

        while not stack_obj.is_empty() and stack_obj.peek() <= num:
            stack_obj.pop()

        if stack_obj.is_empty():
            result.append(-1)
        else:
            result.append(stack_obj.peek())

        stack_obj.push(num)
    return result[::-1]


if __name__ == "__main__":
    print("OUT: ", next_greater_element(nums=[2, 1, 2, 4, 3]))
    print("OUT: ", next_greater_element_using_stack(nums=[2, 1, 2, 4, 3]))
