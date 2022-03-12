# implementation of Stack data structure from 4.5

# if top is at the end of a list
class Stack:

    def __init__(self):
        self._items = []

    # stack operations
    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def is_empty(self):
        return not self._items # empty list returns false 
        # or
        # return self._items == []

    def size(self):
        return len(self._items)

# if top is at the beginning of list
# note: this isn't a formal name because a stack can be in any direction
# note: stack operations are DRASTICALLY slower O(n) compared to O(1) for first implementation
class ReversedStack:
    
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.insert(0, item)
    
    def pop(self):
        return self._items.pop(0)

    def seek(self):
        return self._items[0]

    def is_empty(self):
        return self._items == []

    def size(self):
        return len(self._items)
