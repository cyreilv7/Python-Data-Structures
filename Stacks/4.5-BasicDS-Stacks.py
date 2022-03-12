# see if implementation of Stack data structure is correct
# application of Stack: reverse a string

from stack import Stack

def rev_string(my_str):
    my_stack = Stack()
    for i in my_str:
        my_stack.push(i)
    rev_str = ''
    while not my_stack.is_empty():
        rev_str += (my_stack.pop())
    return rev_str


# s = Stack()

# print(s.is_empty())
# s.push(4)
# s.push("dog")
# print(s.peek())
# s.push(True)
# print(s.size())
# print(s.is_empty())
# s.push(8.4)
# print(s.pop())
# print(s.pop())
# print(s.size())

# s2 = ReversedStack()

# s2 = Stack()
# s2.push("hello")
# s2.push("true")
# print(s2.pop())

print(rev_string("test")) # expected output: tset