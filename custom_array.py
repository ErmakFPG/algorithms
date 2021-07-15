class Array:
    def __init__(self, size):
        self._size = size
        self._collection = [None] * size

    def get_size(self):
        return self._size

    def show_array(self):
        print(self._collection)

    @staticmethod
    def check_position(position, size):
        if position < 0 or position >= size:
            raise IndexError

    def set_value(self, position, value):
        self.check_position(position, self._size)
        self._collection[position] = value

    def get_value(self, position):
        self.check_position(position, self._size)
        return self._collection[position]
