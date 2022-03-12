class Node:
    def __init__(self, data=0):
        self._data = data
        self._next = None

    # getter
    def get_data(self):
        return self._data

    # setter
    def set_data(self, new_data):
        self._data = new_data

    # property (establishes the getter and setter)
    data = property(get_data, set_data)

    def get_next(self):
        return self._next

    def set_next(self, next_node):
        self._next = next_node

    next = property(get_next, set_next)

    def __str__(self):
        return str(self._data)

class LinkedList:
    def __init__(self):
        self.head = None
    
    # add item to beginning of linked list
    def add(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def remove(self, item):
        current = self.head
        previous = None
        while current is not None:
            if current.data == item:
                break
            previous = current
            current = current.next
        if current is None:
            print(f"{item} was not found in the list.")
        elif previous is None:
            self.head = current.next
        else:
            previous.next = current.next
        return

    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def append(self, item):
        pass

    def index(self, item):
        current = self.head
        index = 0
        while current is not None:
            if current.data == item:
                return index
            current = current.next
            index += 1
        raise ValueError(f"{item} is not in the list.")

    def insert(self, pos, item):
        pass

    def pop(self):
        pass

    def pop(self, pos):
        pass

def print_list(linked_lst, label):
    temp = linked_lst.head
    print(label)
    while temp is not None:
        print(temp, end=" ")
        temp = temp.get_next()
    print("\n")

linked_list = LinkedList()
linked_list.add(1)
linked_list.add(2)
linked_list.add(3)
print_list(linked_list, "original list")
linked_list.remove(3)
# linked_list.remove(2)
# linked_list.remove(1)
print_list(linked_list, "list after removal")
print(linked_list.search(3))
print(linked_list.search(2))
print(linked_list.size())
print(linked_list.index(5))
