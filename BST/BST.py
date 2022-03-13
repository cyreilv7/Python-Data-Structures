"""
Utilities of BST:
1) Sort a list of numbers
2) Create a set
3) O(log n) search, insert, delete (assuming it's balanced)

"""
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        # prevent duplicates 
        if data == self.data:
            return
        elif data < self.data:
            if self.left:
                self.left.add_child(data)
            else: # if self.left is a leaf node 
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, target):
        if  target == self.data:
            return True
        if target < self.data:
            if self.left:
                return self.left.search(target)
            else:
                return False
        if target > self.data:
            if self.right:
                return self.right.search(target)
            else:
                return False
    
    def find_height(self):
        if self.left:
            left_height = self.left.find_height()
        else:
            left_height = -1
        if self.right:
            right_height = self.right.find_height()
        else:
            right_height = -1
        return max(left_height, right_height) + 1

    def in_order_traversal(self): # left root right
        elements = [] 
        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()
        # visit root node
        elements.append(self.data)
        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for element in elements:
        root.add_child(element)
    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    root = build_tree(numbers)
    print(root.in_order_traversal())
    print(root.pre_order_traversal())
    print(root.post_order_traversal())
    print(root.search(4))
    print(root.find_height())
