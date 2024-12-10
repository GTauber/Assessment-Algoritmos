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

class BSTWithDelete(BST):
    def delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            min_node = self.find_min_node(root.right)
            root.key = min_node.key
            root.right = self.delete(root.right, min_node.key)
        return root

    def find_min_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current

codes = [45, 25, 65, 20, 30, 60, 70]
bst = BSTWithDelete()
root = None
for code in codes:
    root = bst.insert(root, code)

for code in [20, 25, 45]:
    print(f"Removing code: {code}")
    root = bst.delete(root, code)
    bst.inorder(root)
    print()
