class Cell:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.top = Cell()  # sentinel

    def add_at_end(self, new_cell):
        current_cell = self.top
        while current_cell.next:
            current_cell = current_cell.next
        current_cell.next = new_cell

    def get_max_value(self):
        if not self.top.next:
            return None
        current_cell = max_cell = self.top.next
        while current_cell:
            if max_cell.value < current_cell.value:
                max_cell = current_cell
            current_cell = current_cell.next
        return max_cell.value

    def show(self):
        current_cell = self.top
        current_index = 0
        print('LINKED LIST')
        print('----------')
        while current_cell:
            print(f'{current_index}: {current_cell.value}')
            current_cell = current_cell.next
            current_index += 1
        print('----------')


sample = LinkedList()
sample.add_at_end(Cell(10))
sample.add_at_end(Cell(30))
sample.add_at_end(Cell(20))
sample.show()
print(sample.get_max_value())
