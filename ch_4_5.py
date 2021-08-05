from custom_list import CustomList


class TriangularArray:
    def __init__(self, dimension):
        self._dimension = dimension
        self._one_dimensional_array_size = int((dimension ** 2 + dimension) / 2)
        self._collection = CustomList(self._one_dimensional_array_size)
        for i in range(self._one_dimensional_array_size):
            self._collection.add_value(None)

    def show_collection(self):
        for row in range(self._dimension):
            for column in range(self._dimension):
                if row >= column:
                    print(self.get_value(row, column), end=' ')
            print()

    @staticmethod
    def _convert_to_index(row, column):
        return int((row ** 2 + row) / 2 + column)

    def _check_position(self, row, column):
        if row >= self._dimension or column >= self._dimension:
            raise IndexError

    def get_value(self, row, column):
        self._check_position(row, column)
        if row < column:
            return None
        return self._collection.get_value(self._convert_to_index(row, column))

    def set_value(self, row, column, value):
        self._check_position(row, column)
        if row < column:
            row, column = column, row
        self._collection.set_value(self._convert_to_index(row, column), value)


a = TriangularArray(4)
a.set_value(0, 0, 100)
a.set_value(1, 2, 200)
a.set_value(3, 0, 300)
a.show_collection()
