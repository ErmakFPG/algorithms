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

    def get_value(self, position):
        if position <= self._size:
            return self._collection.get_value(position)
        else:
            raise IndexError

    def set_capacity(self, new_capacity):
        if new_capacity > self._capacity:
            new_collection = Array(new_capacity)
            for position in range(self._size):
                new_collection.set_value(position, self._collection.get_value(position))
            self._collection = new_collection
        elif new_capacity < self._capacity:
            if new_capacity >= self._size:
                new_collection = Array(new_capacity)
                for position in range(new_capacity):
                    new_collection.set_value(position, self._collection.get_value(position))
                self._collection = new_collection
            else:
                raise Exception
        self._capacity = new_capacity

    def add_value(self, value):
        if self._capacity <= self._size:
            self.set_capacity(self._capacity * 2)
        self._collection.set_value(self._size, value)
        self._size += 1

    def remove_value(self, position):
        if position >= self._size:
            raise IndexError
        if self._size == self._capacity:
            self.set_capacity(self._capacity + 1)
        for i in range(position, self._size):
            self._collection.set_value(i, self._collection.get_value(i + 1))
        self._size -= 1
        if self._capacity > 5 * self._size:
            self.set_capacity(int(self._capacity / 2))

    def set_value(self, position, value):
        if position <= self._capacity:
            self.set_capacity(self._capacity + 1)
        else:
            self.set_capacity(position + 1)
        for i in range(self._size, position, -1):
            self._collection.set_value(i, self._collection.get_value(i - 1))
        self._collection.set_value(position, value)
        self._size += 1
