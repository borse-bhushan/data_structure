def selection_sort(array: list):
    size = len(array)

    for i in range(0, size - 1):
        min_index = i

        for j in range(i + 1, size):
            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

    return array


if __name__ == "__main__":
    print("OUT: ", selection_sort([20, 30, 10, 50, 40]))
