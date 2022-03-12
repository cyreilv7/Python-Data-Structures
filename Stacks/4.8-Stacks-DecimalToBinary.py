from stack import Stack

def convert_decimal_to_binary(decimal_num):
    s = Stack()
    binary = ''
    while decimal_num > 0:
        rem = decimal_num % 2
        s.push(rem)
        decimal_num //= 2
    while not s.is_empty():
        binary_digit = s.pop()
        # print(binary_digit)
        binary += str(binary_digit)
    return binary

def convert_decimal_to_base_n(decimal_num, n):
    s = Stack()
    digits = '0123456789ABCDEF' # digits 0 - 15
    base_n = ''
    while decimal_num > 0:
        rem = decimal_num % n
        s.push(rem)
        decimal_num //= n
    while not s.is_empty():
        base_n_digit = digits[s.pop()]
        # print(binary_digit)
        base_n += str(base_n_digit)
    return base_n


print(convert_decimal_to_binary(2)) # expected: 10
print(convert_decimal_to_binary(1)) # expected: 1
print(convert_decimal_to_binary(100)) # expected: 1100100   
print(convert_decimal_to_base_n(25, 8)) # expected: 351
print(convert_decimal_to_base_n(26, 26))