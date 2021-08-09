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

    def insert_cell(self, new_cell):
        if self.top.value == self.bottom.value is None:
            self.top.value = self.bottom.value = new_cell.value
        elif self.top.value == self.bottom.value is not None:
            if new_cell.value >= self.top.value:
                self.bottom.value = new_cell.value
            else:
                self.top.value = new_cell.value
        else:
            if new_cell.value < self.top.value:
                new_cell.next = self.top
                self.top.prev = new_cell
                self.top = new_cell
            elif new_cell.value > self.bottom.value:
                new_cell.prev = self.bottom
                self.bottom.next = new_cell
                self.bottom = new_cell
            else:
                current_cell = self.top
                while current_cell.next.value < new_cell.value:
                    current_cell = current_cell.next
                new_cell.next = current_cell.next
                current_cell.next = new_cell
                new_cell.next.prev = new_cell
                new_cell.prev = current_cell

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
sample.insert_cell(Cell(30))
sample.insert_cell(Cell(20))
sample.insert_cell(Cell(10))
sample.insert_cell(Cell(50))
sample.insert_cell(Cell(40))
sample.show()
sample.show(invert=True)
print(f'top: {sample.top.value}, bottom: {sample.bottom.value}')
