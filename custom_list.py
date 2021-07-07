from custom_array import Array


class CustomList:
    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.collection = Array(capacity)

    def show_collection(self):
        self.collection.show_array()

    def get_size(self):
        return self.size

    def get_capacity(self):
        return self.capacity

    def get_value(self, position):
        if position <= self.size:
            return self.collection.get_value(position)
        else:
            raise IndexError

    def _set_value(self, position, value):
        self.collection.set_value(position, value)

    def set_capacity(self, new_capacity):
        if new_capacity > self.capacity:
            new_collection = Array(new_capacity)
            for position, value in enumerate(self.collection.collection):
                new_collection.set_value(position, value)
            self.collection = new_collection
        elif new_capacity < self.capacity:
            if new_capacity >= self.size:
                new_collection = Array(new_capacity)
                for position in range(new_capacity):
                    new_collection.set_value(position, self.collection.get_value(position))
                self.collection = new_collection
            else:
                raise Exception
        self.capacity = new_capacity

    def add_value(self, value):
        if self.capacity <= self.size:
            self.set_capacity(self.capacity * 2)
        self.collection.set_value(self.size, value)
        self.size += 1

    def remove_value(self, position):
        for i in range(position, self.size):
            self.collection.set_value(position, self.collection.get_value(position + 1))


array = CustomList(5)
array.add_value(10)
array.add_value(20)
array.add_value(30)
print(f'size: {array.get_size()}')
print(f'capacity: {array.get_capacity()}')
array.show_collection()

print('--------------------')

array.add_value(40)
array.add_value(50)
array.add_value(60)
print(f'size: {array.get_size()}')
print(f'capacity: {array.get_capacity()}')
array.show_collection()

print('--------------------')

array.remove_value(1)
array.show_collection()
