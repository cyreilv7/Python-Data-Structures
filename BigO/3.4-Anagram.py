# n^2 solution
def anagram_solution_1(str1, str2):
    is_anagram = True
    if len(str1) != len(str2):
        is_anagram = False
    str2_list = list(str2) # to "check off" a character (i.e., set it to None), string must be converted to a mutable type (e.g., a list)
    str1_index = 0
    while str1_index < len(str1) and is_anagram:
        str2_index = 0
        found = False
        while str2_index < len(str2) and not found:
            if str1[str1_index] == str2_list[str2_index]:
                found = True
                str2_list[str2_index] = None
            else:
                str2_index += 1
        if not found:
            is_anagram = False
        str1_index += 1
    return is_anagram

# n^2 or nlog(n) depending on the sorting algorithm
def anagram_solution_2(str1, str2):
    str1_list = sorted(list(str1))
    str2_list = sorted(list(str2))

    # i = 0
    # is_anagram = True
    # while i < len(str1_list) and is_anagram:
    #     if str1_list[i] == str2_list[i]:
    #         i += 1
    #     else:
    #         is_anagram = False
    # return is_anagram

    for char1, char2 in zip(str1_list, str2_list):
        if char1 != char2:
            return False
    return True

# O(n) solution
def anagram_solution_3(str1, str2):
    c1 = [0]*26 # counter of each possible character in str1
    c2 = [0]*26
    for i in str1:
        pos = ord(i) - ord('a')
        c1[pos] += 1
    for i in str2:
        pos = ord(i) - ord('a')
        c2[pos] += 1
    for pos1, pos2 in zip(c1, c2):
        if pos1 != pos2:
            return False
    return True

print(anagram_solution_2("apple", "pleap"))  # expected: True
print(anagram_solution_2("abcd", "dcba"))  # expected: True
print(anagram_solution_2("abcd", "dcda"))  # expected: False