from stack import Stack

def top_has_precedence(top, operator):
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    return prec[top] > prec[operator]

def infix_to_postfix(infix):
    postfix = ''
    s = Stack()
    operators = '()^*/+-'
    # not sure how to establish precedence
    for token in infix:
        if token not in operators: 
            postfix += token
        elif token == '(':
            s.push(token)
        elif token == ')':
            top_token = s.pop()
            while top_token != '(':
                postfix += top_token
                top_token = s.pop()
        else:
            while not s.is_empty() and top_has_precedence(s.peek(), token):
                postfix += s.pop()
            s.push(token)
    while not s.is_empty():
        postfix += s.pop()
    return postfix

print(infix_to_postfix('A+B*C-D*E')) # expected: ABC*DE*-+
print(infix_to_postfix("A*B+C*D")) # expected: AB*CD*+
print(infix_to_postfix("(A+B)*C-(D-E)*(F+G)")) # expected: AB+C*DE-FG+*-
print(infix_to_postfix("5*3^(4-2)"))

"""
Pseudocode:
1. Iterate over tokens in the infix expression
2. If token isn't an operator, append it to postfix
3. Else if token is an operator and is an open symbol, 
    a. push it to the stack
4. Else if token is any other operator and top of stack is an open symbol
    a. push it to the stack
5. Else if token is a close symbol,
    a. Pop the stack until the top is an open symbol and append it to postfix
    b. Pop the open symbol off stack
6. Else if token is any other operator and top of stack isn't an open symbol,
    a. Pop the stack until top is of lower precedence
"""