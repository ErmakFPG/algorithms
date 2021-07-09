class Array:
    def __init__(self, size):
        self._size = size
        self._collection = [None] * size

    def get_size(self):
        return self._size

    def show_array(self):
        print(self._collection)

    def set_value(self, position, value):
        if position < 0 or position >= self._size:
            raise IndexError
        self._collection[position] = value

    def get_value(self, position):
        if position < 0 or position >= self._size:
            raise IndexError
        return self._collection[position]
