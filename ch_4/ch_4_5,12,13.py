from custom_list import CustomList


class TriangularArray:
    def __init__(self, dimension):
        self._dimension = dimension
        self._one_dimensional_array_size = int((dimension ** 2 + dimension) / 2)
        self._collection = CustomList(self._one_dimensional_array_size)
        for i in range(self._one_dimensional_array_size):
            self._collection.add_value(None)

    def show_collection(self):
        print('---------')
        for row in range(self._dimension):
            for column in range(self._dimension):
                if row >= column:
                    print(self.get_value(row, column), end=' ')
            print()
        print('---------')

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

    def get_dimension(self):
        return self._dimension

    @staticmethod
    def operation(array1, array2, operation_type):
        if array1.get_dimension() != array2.get_dimension():
            raise ValueError
        dimension = array1.get_dimension()
        result_array = TriangularArray(dimension)
        for row in range(dimension):
            for column in range(dimension):
                if row >= column:
                    if operation_type == 'addition':
                        result_array.set_value(row, column,
                                               array1.get_value(row, column) + array2.get_value(row, column))
                    if operation_type == 'multiply':
                        value = 0
                        for k in range(dimension):
                            el1 = array1.get_value(row, k)
                            el2 = array2.get_value(k, column)
                            if el1 is None:
                                el1 = 0
                            if el2 is None:
                                el2 = 0
                            value += el1 * el2
                        result_array.set_value(row, column, value)
        return result_array


a1 = TriangularArray(3)
a2 = TriangularArray(3)
for i in range(3):
    for j in range(3):
        a1.set_value(i, j, 30)
        a2.set_value(i, j, 50)
a3 = TriangularArray.operation(a1, a2, 'addition')
a4 = TriangularArray.operation(a1, a2, 'multiply')
a1.show_collection()
a2.show_collection()
a3.show_collection()
a4.show_collection()
