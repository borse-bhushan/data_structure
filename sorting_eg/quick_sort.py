def partition(array: list, start, end):
    pivot = array[end]
    st_ind = start - 1

    for i in range(start, end):
        if array[i] < pivot:
            st_ind += 1
            array[i], array[st_ind] = array[st_ind], array[i]

    st_ind += 1
    array[st_ind], array[end] = array[end], array[st_ind]

    return st_ind


def quick_sort(array: list, start, end):

    if start >= end:
        return

    pivot = partition(array, start, end)
    quick_sort(array, start, pivot - 1)
    quick_sort(array, pivot + 1, end)

    return array


if __name__ == "__main__":
    array = [20, 30, 10, 50, 40]
    print("OUT: ", quick_sort(array, 0, len(array) - 1))
