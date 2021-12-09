from custom_list import CustomList


def swap(array, index1, index2):
    temp = array.get_value(index1)
    array.set_value(index1, array.get_value(index2))
    array.set_value(index2, temp)


def effective_bubble_sort(array):
    not_sorted = True
    reverse = False
    left_limit = 0
    right_limit = array.get_size() - 1

    while not_sorted:
        not_sorted = False
        if not reverse:
            for i in range(left_limit, right_limit):
                if array.get_value(i) > array.get_value(i + 1):
                    swap(array, i, i + 1)
                    not_sorted = True
                    right_limit = i
            if not_sorted:
                reverse = True
        if reverse:
            for i in range(right_limit, left_limit, -1):
                if array.get_value(i) < array.get_value(i - 1):
                    swap(array, i, i - 1)
                    not_sorted = True
                    left_limit = i
            if not_sorted:
                reverse = False


a = CustomList(6)
a.add_value(4)
a.add_value(1)
a.add_value(3)
a.add_value(7)
a.add_value(5)
a.add_value(2)
a.show_collection()
effective_bubble_sort(a)
a.show_collection()
