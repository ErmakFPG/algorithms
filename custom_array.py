class Array:
    def __init__(self, size):
        self.size = size
        self.collection = [None] * size

    def get_size(self):
        return self.size

    def show_array(self):
        print(self.collection)

    def set_value(self, position, value):
        if position < 0 or position >= self.size:
            raise IndexError
        self.collection[position] = value

    def get_value(self, position):
        if position < 0 or position >= self.size:
            raise IndexError
        return self.collection[position]
