class Cell:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.top = Cell(None)  # limiter

    def add_at_beginning(self, new_cell):
        new_cell.next = self.top.next
        self.top.next = new_cell

    def add_at_end(self, new_cell):
        current_cell = self.top
        while current_cell.next:
            current_cell = current_cell.next
        current_cell.next = new_cell

    @staticmethod
    def insert_cell(after_me, new_cell):
        new_cell.next = after_me.next
        after_me.next = new_cell

    @staticmethod
    def delete_after(after_me):
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
