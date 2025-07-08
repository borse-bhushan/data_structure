def binary_search(value, sorted_list):

    if not sorted_list:
        return False, ""

    print("SEARCHING FOR: ", value)

    start_index = 0
    end_index = len(sorted_list) - 1


    while not start_index > end_index:

        mid_index = (start_index + end_index) // 2

        mid_val = sorted_list[mid_index]
        if value == mid_val:
            return True, f"At {mid_index}"

        if mid_val < value:
            start_index = mid_index + 1

        if mid_val > value:
            end_index = mid_index - 1

    return False, ""



sorted_list = sorted([10, 20, 30, 40, 90])

for i in sorted_list + [5, 31, 45, 56]:
    print(
        "FOUND: ", binary_search(i, sorted_list), "\n\n"
    )
