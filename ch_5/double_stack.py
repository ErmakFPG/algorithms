from custom_list import CustomList


class DoubleStack:
    def __init__(self, capacity):
        self._collection = CustomList(capacity)
        self._next_index1 = 0
        self._next_index2 = capacity - 1
        for i in range(capacity):
            self._collection.add_value(None)

    def push1(self, value):
        if self._next_index1 > self._next_index2:
            raise IndexError
        self._collection.set_value(self._next_index1, value)
        self._next_index1 += 1

    def push2(self, value):
        if self._next_index1 > self._next_index2:
            raise IndexError
        self._collection.set_value(self._next_index2, value)
        self._next_index2 -= 1

    def pop1(self):
        if self._next_index1 == 0:
            raise IndexError
        self._next_index1 -= 1
        remove_value = self._collection.get_value(self._next_index1)
        self._collection.set_value(self._next_index1, None)
        return remove_value

    def pop2(self):
        if self._next_index2 == self._collection.get_capacity() - 1:
            raise IndexError
        self._next_index2 += 1
        remove_value = self._collection.get_value(self._next_index2)
        self._collection.set_value(self._next_index2, None)
        return remove_value

    def show(self):
        self._collection.show_collection()


if __name__ == '__main__':
    sample = DoubleStack(6)
    sample.push1(10)
    sample.push1(20)
    sample.push2(30)
    sample.push2(40)
    sample.show()
