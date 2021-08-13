from custom_list import CustomList


class Stack:
    def __init__(self, capacity):
        self._collection = CustomList(capacity)
        self._next_index = 0

    def push(self, value):
        if self._next_index == self._collection.get_capacity():
            raise MemoryError
        self._collection.add_value(value)
        self._next_index += 1

    def pop(self):
        if self._next_index == 0:
            raise IndexError
        self._next_index -= 1
        return self._collection.remove_value(self._next_index)

    def show(self):
        self._collection.show_collection()

    @staticmethod
    def reverse_array(array):
        array_size = array.get_size()
        stack = Stack(array_size)
        for i in range(array_size):
            stack.push(array.get_value(i))
        for i in range(array_size):
            array.set_value(i, stack.pop())


if __name__ == '__main__':
    sample = CustomList(3)
    sample.add_value(10)
    sample.add_value(20)
    sample.add_value(30)
    Stack.reverse_array(sample)
    sample.show_collection()
