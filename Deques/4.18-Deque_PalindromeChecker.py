from deque import Deque

def check_palindrome(test_str):
    deque = Deque()
    for char in test_str:
        deque.add_front(char)
    
    while deque.size() > 1:
        if deque.remove_front() != deque.remove_rear():
            return False
    return True

print(check_palindrome("lsdkjfskf"))
print(check_palindrome("radar")) 