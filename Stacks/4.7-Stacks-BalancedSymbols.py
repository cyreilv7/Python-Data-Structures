# implementation of stack: 
# check if a string of symbols (not just parentheses) is balanced 
from stack import Stack

def is_matching_symbol(top, symb):
    cond1 = top == '(' and symb == ')'
    cond2 = top == '[' and symb == ']'
    cond3 = top == '{' and symb == '}'
    return cond1 or cond2 or cond3

def check_balanced_symbols(my_str):
    stack = Stack()
    open_symbols = ['(', '[', '{']
    for symbol in my_str:
        if symbol in open_symbols:
            stack.push(symbol)
        else:
            if stack.is_empty():
                return False
            top = stack.pop()
            if not is_matching_symbol(top, symbol):
                return False
    return stack.is_empty()

print(check_balanced_symbols('[[]]')) # expected: True
print(check_balanced_symbols('[)')) # expected: False
print(check_balanced_symbols('')) # expected: True
print(check_balanced_symbols('[')) # expected: False
print(check_balanced_symbols(']')) # expected: False
print(check_balanced_symbols('{({([][])}())}')) # expected: True
print(check_balanced_symbols('[{()]')) # expected: False

"""
Pseudocode:
1. Loop through each symbol in the string
2. If open symbol, push to stack
3. If close symbol, check if top item on stack as its corresponding open symbol
4. Else, return False
5. If close symbol but stack is empty, return False
6. End of loop, if stack is empty, return True
7. Else return False 
"""
