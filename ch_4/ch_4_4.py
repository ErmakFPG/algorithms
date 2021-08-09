def insert_item(array, value, position):
    length_array = array.get_size()
    if position > length_array - 1:
        raise IndexError
    array.set_capacity(array.get_capacity() + 1)
    for i in range(length_array - 1, position - 1, -1):
        array.set_value(i + 1, array.get_value(i))
    array.set_value(position, value)


def delete_item(array, position):
    length_array = array.get_size()
    if position > length_array - 1:
        raise IndexError
    for i in range(position, length_array - 1):
        array.set_value(i, array.get_value(i + 1))
    array.remove_value(length_array - 1)
    array.set_capacity(array.get_capacity() - 1)
