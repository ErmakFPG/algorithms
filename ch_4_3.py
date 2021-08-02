def median(array):
    length_array = array.get_size()

    if length_array % 2 == 0:
        return (array.get_value(int(length_array / 2 - 1)) + array.get_value(int(length_array / 2))) / 2
    else:
        return array.get_value(int(length_array / 2))
