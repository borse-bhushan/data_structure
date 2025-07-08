
def linear_search(data, search_value):
    if not data:
        return False, ""

    for index, current_value in enumerate(data):
        if search_value == current_value:
            return True, f"At index {index}"
    return False, ""

data_list = [1, 2, 3]

print("FOUND: ", *linear_search(data_list, 2))
print("FOUND: ", *linear_search(data_list, 5))
