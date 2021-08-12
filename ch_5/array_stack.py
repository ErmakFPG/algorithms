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


if __name__ == '__main__':
    sample = Stack(5)
    sample.push(10)
    sample.push(20)
    sample.push(30)
    sample.show()
    print(sample.pop())
    sample.show()
