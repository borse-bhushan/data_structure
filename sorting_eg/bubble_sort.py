def bb_s(array: list):

    if not array:
        return []

    size = len(array)
    if size == 1:
        return array

    for i in range(0, size - 1):
        swapped = False

        for j in range(0, (size - 1) - i):

            if array[j] > array[j + 1]:
                swapped = True
                array[j], array[j + 1] = array[j + 1], array[j]

        if not swapped:
            break

    return array


if __name__ == "__main__":
    print("OUT: ", bb_s([20, 30, 10, 50, 40]))
