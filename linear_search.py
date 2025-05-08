
def linear_search(data, search_value):
    if not data:
        return False

    for index, current_value in enumerate(data):
        if search_value == current_value:
            return index
    return False

data_list = [1, 2, 3]

print(linear_search(data_list, 2))
print(linear_search(data_list, 5))
