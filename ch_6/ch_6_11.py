from custom_list import CustomList
from ch_5.array_stack import Stack


def quick_sort_custom_stack(array, start, end):
    if start >= end:
        return

    divider = array.get_value(start)
    before = Stack(end)
    after = Stack(end)
    for i in range(start + 1, end + 1):
        current_value = array.get_value(i)
        if current_value < divider:
            before.push(current_value)
        else:
            after.push(current_value)

    index = start
    while before.has_items():
        array.set_value(index, before.pop())
        index += 1
    array.set_value(index, divider)
    midpoint = index
    index += 1
    while after.has_items():
        array.set_value(index, after.pop())
        index += 1

    quick_sort_custom_stack(array, start, midpoint - 1)
    quick_sort_custom_stack(array, midpoint + 1, end)


if __name__ == '__main__':
    sample = CustomList(6)
    sample.add_value(3)
    sample.add_value(2)
    sample.add_value(3)
    sample.add_value(1)
    sample.add_value(2)
    sample.add_value(6)
    sample.show_collection()
    quick_sort_custom_stack(sample, 0, 5)
    sample.show_collection()
