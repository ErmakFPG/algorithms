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

    @staticmethod
    def insert_cell(after_me, new_cell):
        new_cell.next = after_me.next
        after_me.next = new_cell
        new_cell.next.prev = new_cell
        new_cell.prev = after_me

    def add_at_beginning(self, new_cell):
        LinkedList.insert_cell(self.top, new_cell)

    def add_at_end(self, new_cell):
        LinkedList.insert_cell(self.bottom.prev, new_cell)

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
sample.add_at_end(Cell(10))
sample.add_at_end(Cell(20))
sample.add_at_end(Cell(30))
sample.show()
sample.show(invert=True)
