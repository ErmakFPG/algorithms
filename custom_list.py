from custom_array import Array


class CustomList:
    def __init__(self, capacity):
        self._size = 0
        self._capacity = capacity
        self._collection = Array(capacity)

    def show_collection(self):
        self._collection.show_array()

    def get_size(self):
        return self._size

    def get_capacity(self):
        return self._capacity

    def _check_position(self, position):
        if position < 0 or position >= self._size:
            raise IndexError

    def get_value(self, position):
        self._check_position(position)
        return self._collection.get_value(position)

    def set_value(self, position, value):
        self._check_position(position)
        self._collection.set_value(position, value)

    def _copy_values_in_new_collection(self, new_capacity):
        new_collection = Array(new_capacity)
        for position in range(self._size):
            new_collection.set_value(position, self._collection.get_value(position))
        self._collection = new_collection
        self._capacity = new_capacity

    def set_capacity(self, new_capacity):
        if new_capacity == self._capacity:
            return
        if new_capacity < self._size:
            raise ValueError
        self._copy_values_in_new_collection(new_capacity)

    def add_value(self, value):
        if self._capacity == 0:
            self.set_capacity(1)
        if self._capacity == self._size:
            self.set_capacity(self._capacity * 2)
        self._collection.set_value(self._size, value)
        self._size += 1

    def remove_value(self, position):
        self._check_position(position)
        delete_value = self._collection.get_value(position)
        for i in range(position, self._size - 1):
            self._collection.set_value(i, self._collection.get_value(i + 1))
        self._collection.set_value(self._size - 1, None)
        self._size -= 1
        if self._capacity > 5 * self._size:
            self.set_capacity(int(self._capacity / 2))
        return delete_value

    def add_list(self, added_list):
        for i in range(added_list.get_size()):
            self.add_value(added_list.get_value(i))


if __name__ == '__main__':
    sample = CustomList(0)
    sample.add_value(10)
    sample.add_value(20)
    sample.add_value(30)
    sample.add_value(40)
    sample.add_value(50)
    sample.show_collection()
