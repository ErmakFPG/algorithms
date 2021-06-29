def median(array):
    length_array = len(array)

    if length_array % 2 == 0:
        return (array[int(length_array / 2 - 1)] + array[int(length_array / 2)]) / 2

    else:
        return array[int(length_array / 2)]


print(median([1, 2, 4, 6]))
print(median([1, 2, 3, 7, 1000]))
