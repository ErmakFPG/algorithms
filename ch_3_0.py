class Node:
    def __init__(self, value=None):
        self.value = value
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_contain(self, value):
        current_node = self.head
        while current_node:
            if value == current_node.value:
                return True
            else:
                current_node = current_node.next_node
        return False

    def add_node(self, new_value):
        new_node = Node(new_value)
        if not self.head:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next_node:
            current_node = current_node.next_node
        current_node.next_node = new_node

    def get(self, value_index):
        current_node = self.head
        current_index = 0
        while current_node:
            if current_index == value_index:
                return current_node.value
            elif current_node.next_node:
                current_index += 1
                current_node = current_node.next_node
            else:
                return 'Index out of range'
        return 'Linked list is empty'

    def remove_node(self, remove_index):
        current_node = self.head
        current_index = 0

        while current_node:
            if remove_index == 0:
                if current_node.next_node:
                    self.head = current_node.next_node
                else:
                    self.head = None
                break

            if current_index == remove_index:
                previous_node.next_node = current_node.next_node
                break
            elif current_node.next_node:
                previous_node = current_node
                current_node = current_node.next_node
                current_index += 1
            else:
                return 'Index out of range'

    def show(self):
        current_node = self.head
        current_index = 0
        print('LINKED LIST')
        print('----------')
        while current_node:
            print(f'{current_index}: {current_node.value}')
            if current_node.next_node:
                current_node = current_node.next_node
                current_index += 1
            else:
                print('----------')
                return
        print('----------')
