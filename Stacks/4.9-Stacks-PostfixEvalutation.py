from stack import Stack

def evaluate_subexp(operator, op1, op2):
    if operator == '+':
        return op2 + op1
    elif operator == '-':
        return op2 - op1
    elif operator == '*':
        return op2 * op1
    else:
        return op2 / op1

def evaluate_postfix(exp):
    postfix = exp.split(' ')
    s = Stack()
    for token in postfix:
        if token in '0123456789':
            s.push(int(token))
        else:
            operand1 = s.pop()
            operand2 = s.pop()
            s.push(evaluate_subexp(token, operand1, operand2))
    return s.pop()

print(evaluate_postfix('7 8 + 3 2 + /')) # expected: 3.0