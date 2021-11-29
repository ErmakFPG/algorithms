class Cell:
    def __init__(self, value=None, priority='low'):
        self.value = value
        self.next = None
        self.prev = None
        self.priority = priority


class Deque:
    def __init__(self):
        self.top = Cell()  # top sentinel
        self.bottom = Cell()  # bottom sentinel
        self.top.next = self.bottom
        self.bottom.prev = self.top

    def enqueue(self, new_cell):
        if new_cell.priority == 'low':
            new_cell.next = self.bottom
            self.bottom.prev.next = new_cell
            new_cell.prev = self.bottom.prev
            self.bottom.prev = new_cell
        elif new_cell.priority == 'high':
            self.top.next.prev = new_cell
            new_cell.prev = self.top
            new_cell.next = self.top.next
            self.top.next = new_cell
        else:
            raise AttributeError

    def dequeue(self):
        if self.top.next == self.bottom:
            raise IndexError
        delete_value = self.top.next.value
        self.top.next = self.top.next.next
        self.top.next.prev = self.top
        return delete_value

    def show(self):
        current_cell = self.top
        current_index = 0
        print('LINKED LIST')
        print('----------')
        while current_cell:
            print(f'{current_index}: {current_cell.value} (priority = {current_cell.priority})')
            current_cell = current_cell.next
            current_index += 1
        print('----------')
