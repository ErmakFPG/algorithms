class Cell:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = Cell()  # sentinel

    def push(self, new_cell):
        new_cell.next = self.top.next
        self.top.next = new_cell

    def pop(self):
        if self.top is None:
            raise IndexError
        result = self.top.next.value
        self.top.next = self.top.next.next
        return result

    def show(self):
        current_cell = self.top
        current_index = 0
        print('STACK')
        print('----------')
        while current_cell:
            print(f'{current_index}: {current_cell.value}')
            current_cell = current_cell.next
            current_index += 1
        print('----------')


if __name__ == '__main__':
    sample = Stack()
    sample.push(Cell(10))
    sample.push(Cell(20))
    sample.push(Cell(30))
    sample.show()
