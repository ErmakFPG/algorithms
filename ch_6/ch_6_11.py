from custom_list import CustomList
from ch_5.array_stack import Stack


def quick_sort(array):
    divider = array.get_value(0)
    stack_capacity = array.get_size()
    stack_before = Stack(stack_capacity)
    stack_after = Stack(stack_capacity)
    for i in range(1, stack_capacity):
        current_value = array.get_value(i)
        if current_value < divider:
            stack_before.push(current_value)
        else:
            stack_after.push(current_value)
    j = 0
    while stack_before.has_items():
        array.set_value(j, stack_before.pop())
        j += 1
    array.set_value(j, divider)
    j += 1
    while stack_after.has_items():
        array.set_value(j, stack_after.pop())
        j += 1


if __name__ == '__main__':
    sample = CustomList(5)
    sample.add_value(3)
    sample.add_value(5)
    sample.add_value(1)
    sample.add_value(8)
    sample.add_value(2)
    sample.show_collection()
    quick_sort(sample)
    sample.show_collection()
