def merge(first_part, second_part):

    results = []

    while first_part and second_part:
        if first_part[0] > second_part[0]:
            results.append(second_part.pop(0))
        else:
            results.append(first_part.pop(0))

    results += first_part
    results += second_part

    return results


def merge_sort(array: list):
    if not array:
        return array

    size = len(array)
    if size == 1:
        return array

    mid = size // 2

    second_part = merge_sort(array[mid:])
    first_part = merge_sort(array[:mid])

    results = []
    results += merge(first_part, second_part)

    return results


if __name__ == "__main__":
    print("OUT", merge_sort([20, 30, 10, 50, 40]))
