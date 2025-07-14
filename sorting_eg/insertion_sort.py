def insertion_sort(array: list):
    size = len(array)

    for i in range(1, size):
        current = array[i]

        j = i - 1
        while j >= 0 and array[j] > current:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current

    return array


if __name__ == "__main__":
    print("OUT: ", insertion_sort([30, 10, 40, 20, 50]))
