"""
Write two Python functions to find the minimum number in a list. The first function should compare each number to every other number on the list. (O^n2). The second function should be linear. O(n)
"""

# O(n^2) solution
# def find_min_n2(lst):
#     for i in lst:
#         nums_greater_than = 0
#         for j in lst:
#             if i <= j:
#                 nums_greater_than += 1
#                 if nums_greater_than == len(lst):
#                     return i
def find_min_n2(lst):
    min = lst[0]
    for i in lst:
        is_smallest = True
        for j in lst:
            if i > j:
                is_smallest = False
        if is_smallest:
            min = i
    return min

# O(n) solution
def find_min_n(lst):
    min = lst[0]
    for i in lst:
        if i < min:
            min = i
    return min

def main():
    my_lst = [5, 3, 3, 7, 8, 2, 0, 3,]
    print(find_min_n(my_lst))
    print(find_min_n2(my_lst))

if __name__ == '__main__':
    main()

