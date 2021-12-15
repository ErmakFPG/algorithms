from custom_list import CustomList


class PriorityQueue:
    def __init__(self, value_list, priority_list):
        self.value_list = value_list
        self.priority_list = priority_list
        self.make_heap()

    @staticmethod
    def swap(array, index1, index2):
        temp = array.get_value(index1)
        array.set_value(index1, array.get_value(index2))
        array.set_value(index2, temp)

    def make_heap(self):
        if self.value_list.get_size() != self.priority_list.get_size():
            raise ValueError
        for i in range(self.priority_list.get_size()):
            index = i
            while index:
                parent = int((index - 1) / 2)
                if self.priority_list.get_value(index) <= self.priority_list.get_value(parent):
                    break
                self.swap(self.value_list, index, parent)
                self.swap(self.priority_list, index, parent)
                index = parent

    def enqueue(self, value, priority):
        self.value_list.add_value(value)
        self.priority_list.add_value(priority)
        index = self.value_list.get_size() - 1
        while index:
            parent = int((index - 1) / 2)
            if self.priority_list.get_value(index) <= self.priority_list.get_value(parent):
                break
            self.swap(self.value_list, index, parent)
            self.swap(self.priority_list, index, parent)
            index = parent

    def dequeue(self):
        result = self.value_list.get_value(0)
        size = self.value_list.get_size()
        self.value_list.set_value(0, self.value_list.get_value(size - 1))
        self.priority_list.set_value(0, self.priority_list.get_value(size - 1))
        self.value_list.remove_value(size - 1)
        self.priority_list.remove_value(size - 1)
        index = 0
        while True:
            child1 = 2 * index + 1
            child2 = 2 * index + 2
            if child1 >= size - 1:
                child1 = index
            if child2 >= size - 1:
                child2 = index

            if self.priority_list.get_value(index) >= self.priority_list.get_value(
                    child1) and self.priority_list.get_value(index) >= self.priority_list.get_value(child2):
                break

            if self.priority_list.get_value(child1) > self.priority_list.get_value(child2):
                swap_child = child1
            else:
                swap_child = child2

            self.swap(self.value_list, index, swap_child)
            self.swap(self.priority_list, index, swap_child)
            index = swap_child

        return result

    def show_lists(self):
        self.value_list.show_collection()
        self.priority_list.show_collection()


if __name__ == '__main__':
    my_list1 = CustomList(7)
    my_list2 = CustomList(7)
    my_list1.add_value(10)
    my_list1.add_value(20)
    my_list1.add_value(30)
    my_list1.add_value(40)
    my_list1.add_value(50)
    my_list1.add_value(60)
    my_list1.add_value(70)
    my_list2.add_value(1)
    my_list2.add_value(5)
    my_list2.add_value(7)
    my_list2.add_value(6)
    my_list2.add_value(2)
    my_list2.add_value(4)
    my_list2.add_value(3)
    sample = PriorityQueue(my_list1, my_list2)
    sample.show_lists()
    sample.dequeue()
    sample.show_lists()
    sample.enqueue(80, 8)
    sample.show_lists()
