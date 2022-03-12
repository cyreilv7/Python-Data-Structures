# implementation of stack: 
# checks if a string of parentheses is balanced (i.e., there is a closing parenthesis for every opening parenthesis)
from stack import Stack

def is_balanced(my_str):
    my_stack = Stack()
    for i in my_str:
        if i == '(':
            my_stack.push(i)
        else:
            if my_stack.is_empty(): # if current i = ')' and there are no '(' in our stack, the string is unbalanced 
                return False
            my_stack.pop()
    return my_stack.is_empty() # a string of parenthesis is balanced if the stack is empty


print(is_balanced('()')) # expected: True
print(is_balanced('(()')) # expected: False
print(is_balanced('((((()')) # expected: False
# edge cases
print(is_balanced('(')) # expected: False
print(is_balanced(')')) # expected: False