def insert_item(array, value, position):
    if position > len(array):
        raise IndexError
    return array[:position] + [value] + array[position:]


def remove_item(array, position):
    if position > len(array):
        raise IndexError
    return array[:position] + array[position + 1:]


print(insert_item([1, 2, 3, 4], 5, 4))
print(remove_item([1, 2, 3, 4, 5], 4))
