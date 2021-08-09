class Cell:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.top = Cell()  # sentinel
        self.bottom = self.top

    def add_to_end(self, new_cell):
        self.bottom.next = new_cell
        self.bottom = new_cell

    def delete_after(self, after_me):
        if after_me == self.bottom:
            print("Cell doesn't exist")
        elif after_me.next == self.bottom:
            self.bottom = after_me
            after_me.next = None
        else:
            after_me.next = after_me.next.next

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
cell1 = Cell(10)
cell2 = Cell(20)
cell3 = Cell(30)
sample.add_to_end(cell1)
sample.add_to_end(cell2)
sample.add_to_end(cell3)

sample.show()
print(f'old bottom: {sample.bottom.value}')

sample.delete_after(cell2)

sample.show()
print(f'new bottom: {sample.bottom.value}')
