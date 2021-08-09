from custom_list import CustomList


class TwoDimensionalArray:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self.dimension = width * height
        self._collection = CustomList(self.dimension)
        for i in range(self.dimension):
            self._collection.add_value(None)

    def show_collection(self):
        for row in range(self._height):
            for column in range(self._width):
                print(self.get_value(row, column), end=' ')
            print()

    def _convert_to_index(self, row, column):
        return row * self._width + column

    def _check_position(self, row, column):
        if row >= self._height or column >= self._width:
            raise IndexError

    def get_value(self, row, column):
        self._check_position(row, column)
        return self._collection.get_value(self._convert_to_index(row, column))

    def set_value(self, row, column, value):
        self._check_position(row, column)
        self._collection.set_value(self._convert_to_index(row, column), value)

    def _make_magic(self, magic_type):
        for row in range(self._height):
            for column in range(self._width):
                if magic_type == 'true_magic':
                    if row > column:
                        self.set_value(row, column, 1)
                    else:
                        self.set_value(row, column, 0)
                if magic_type == 'reverse_magic':
                    if row + column <= self._width - 1:
                        self.set_value(row, column, 1)
                    else:
                        self.set_value(row, column, 0)

    def make_true_magic(self):
        self._make_magic('true_magic')

    def make_reverse_magic(self):
        self._make_magic('reverse_magic')

    def make_ultimate_magic(self):
        for row in range(self._height):
            for column in range(self._width):
                self.set_value(row, column, min(row, column, self._height - row - 1, self._width - column - 1))


a = TwoDimensionalArray(5, 4)
a.make_true_magic()
a.show_collection()
print('------------')
a.make_reverse_magic()
a.show_collection()
print('------------')
a.make_ultimate_magic()
a.show_collection()
