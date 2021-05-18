class Cell:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.top = Cell()  # top sentinel
        self.bottom = Cell()  # bottom sentinel
        self.top.next = self.bottom
        self.bottom.prev = self.top

    def add_at_beginning(self, new_cell):
        new_cell.next = self.top.next
        self.top.next = new_cell
        new_cell.next.prev = new_cell
        new_cell.prev = self.top

    def add_at_end(self, new_cell):
        new_cell.prev = self.bottom.prev
        self.bottom.prev = new_cell
        new_cell.prev.next = new_cell
        new_cell.next = self.bottom

    def show(self, invert=False):
        if invert:
            current_cell = self.bottom
        else:
            current_cell = self.top
        current_index = 0
        print('LINKED LIST')
        print('----------')
        while current_cell:
            print(f'{current_index}: {current_cell.value}')
            if invert:
                current_cell = current_cell.prev
            else:
                current_cell = current_cell.next
            current_index += 1
        print('----------')


sample = LinkedList()
sample.add_at_beginning(Cell(30))
sample.add_at_beginning(Cell(20))
sample.add_at_beginning(Cell(10))
sample.show()
sample.show(invert=True)
