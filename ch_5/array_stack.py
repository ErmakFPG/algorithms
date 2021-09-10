from custom_list import CustomList


class Stack:
    def __init__(self, capacity):
        self._collection = CustomList(capacity)
        self._capacity = capacity
        self._next_index = 0

    def push(self, value):
        if self._next_index == self._capacity:
            raise MemoryError
        self._collection.add_value(value)
        self._next_index += 1

    def pop(self):
        if self._next_index == 0:
            raise IndexError
        self._next_index -= 1
        return self._collection.remove_value(self._next_index)

    def get_value(self, position):
        return self._collection.get_value(position)

    def has_items(self):
        if self._next_index:
            return True
        return False

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

    def insertion_sort(self):
        temp_stack = Stack(self._capacity)
        while self.has_items():
            next_item = self.pop()
            while temp_stack.has_items() and next_item > temp_stack.get_value(temp_stack._next_index - 1):
                self.push(temp_stack.pop())
            temp_stack.push(next_item)
        while temp_stack.has_items():
            self.push(temp_stack.pop())

    @staticmethod
    def selection_sort():
        print('I have no idea how to do it')


if __name__ == '__main__':
    sample = Stack(3)
    sample.push(30)
    sample.push(10)
    sample.push(20)
    sample.show()
