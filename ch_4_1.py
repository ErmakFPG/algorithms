def dispersion(array):
    average = 0
    length_array = len(array)
    for el in array:
        average += el
    average /= length_array

    result = 0
    for el in array:
        result += (el - average) ** 2
    result /= length_array

    return result


print(dispersion([1, 2, 3, 4, 100]))  # 1522
