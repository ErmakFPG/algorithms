def dispersion(array):
    average = 0
    length_array = array.get_size()
    for i in range(length_array):
        average += array.get_value(i)
    average /= length_array

    result = 0
    for i in range(length_array):
        result += (array.get_value(i) - average) ** 2
    result /= length_array

    return result
