from custom_list import CustomList


def insertion_sort(array):
    for i in range(array.get_size()):
        for j in range(0, i):
            if array.get_value(j) > array.get_value(i):
                insert_value = array.get_value(i)
                for k in range(i - 1, j - 1, -1):
                    array.set_value(k + 1, array.get_value(k))
                array.set_value(j, insert_value)
                break


def selection_sort(array):
    for i in range(array.get_size()):
        min_value = array.get_value(i)
        min_index = i
        for j in range(i + 1, array.get_size()):
            if array.get_value(j) < min_value:
                min_value = array.get_value(j)
                min_index = j
        if min_index != i:
            temp_value = array.get_value(i)
            array.set_value(i, min_value)
            array.set_value(min_index, temp_value)


a = CustomList(6)
a.add_value(4)
a.add_value(1)
a.add_value(3)
a.add_value(7)
a.add_value(5)
a.add_value(2)
a.show_collection()
insertion_sort(a)
a.show_collection()
