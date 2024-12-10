class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

class BSTWithMinMax(BST):
    def find_min(self, root):
        current = root
        while current.left:
            current = current.left
        return current.key

    def find_max(self, root):
        current = root
        while current.right:
            current = current.right
        return current.key

grades = [85, 70, 95, 60, 75, 90, 100]
bst = BSTWithMinMax()
root = None
for grade in grades:
    root = bst.insert(root, grade)

min_grade = bst.find_min(root)
max_grade = bst.find_max(root)
print(f"Nota mínima: {min_grade}")
print(f"Nota máxima: {max_grade}")
