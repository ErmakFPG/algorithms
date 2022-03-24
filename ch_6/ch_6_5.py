from custom_list import CustomList


def bubble_sort(array):
    not_sorted = True
    while not_sorted:
        not_sorted = False
        for i in range(array.get_size() - 1):
            if array.get_value(i) > array.get_value(i + 1):
                temp = array.get_value(i)
                array.set_value(i, array.get_value(i + 1))
                array.set_value(i + 1, temp)
                not_sorted = True


if __name__ == '__main__':
    a = CustomList(6)
    a.add_value(4)
    a.add_value(1)
    a.add_value(3)
    a.add_value(7)
    a.add_value(5)
    a.add_value(2)
    a.show_collection()
    bubble_sort(a)
    a.show_collection()
