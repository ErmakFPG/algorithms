from custom_list import CustomList


def swap(array, index1, index2):
    temp = array.get_value(index1)
    array.set_value(index1, array.get_value(index2))
    array.set_value(index2, temp)


def make_heap(array, count):
    for i in range(count):
        index = i
        while index:
            parent = int((index - 1) / 2)
            if array.get_value(index) <= array.get_value(parent):
                break
            swap(array, index, parent)
            index = parent


def heap_sort(array):
    count = array.get_size()
    make_heap(array, count)
    for i in range(array.get_size() - 1, 0, -1):
        swap(array, 0, i)
        count -= 1
        make_heap(array, count)


if __name__ == '__main__':
    sample = CustomList(5)
    sample.add_value(4)
    sample.add_value(1)
    sample.add_value(3)
    sample.add_value(5)
    sample.add_value(2)
    sample.show_collection()
    heap_sort(sample)
    sample.show_collection()
