class Cell:
    def __init__(self, value=None, priority=0):
        self.value = value
        self.next = None
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.top = Cell()  # sentinel

    def enqueue(self, new_cell):
        new_cell.next = self.top.next
        self.top.next = new_cell

    def dequeue(self):
        if self.top.next is None:
            raise IndexError

        current_cell = delete_after = self.top
        top_priority = 0

        while current_cell.next:
            if current_cell.next.priority >= top_priority:
                delete_after = current_cell
                top_priority = current_cell.next.priority
            current_cell = current_cell.next

        delete_value = delete_after.next.value
        delete_after.next = delete_after.next.next

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
