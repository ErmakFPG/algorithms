class Array:
    def __init__(self, size):
        self._size = size
        self._collection = [None] * size

    def get_size(self):
        return self._size

    def show_array(self):
        print(self._collection)

    def check_position(self, position):
        if position < 0 or position >= self._size:
            raise IndexError

    def set_value(self, position, value):
        self.check_position(position)
        self._collection[position] = value

    def get_value(self, position):
        self.check_position(position)
        return self._collection[position]
