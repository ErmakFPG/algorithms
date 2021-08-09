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

    def is_sorted_1(self):
        current_cell = self.top.next
        while current_cell:
            if current_cell.next and current_cell.value > current_cell.next.value:
                return False
            current_cell = current_cell.next
        return True

    def is_sorted_2(self):
        if self.top.next is None:
            return True
        if self.top.next.next is None:
            return True
        current_cell = self.top.next
        while current_cell.next:
            if current_cell.value > current_cell.next.value:
                return False
            current_cell = current_cell.next
        return True


sample = LinkedList()
sample.add_at_end(Cell(10))
sample.add_at_end(Cell(30))
sample.add_at_end(Cell(20))
print(sample.is_sorted_1())
