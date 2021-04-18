# BST tree algorithm

class BSTNode:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if not self.data:
            return BSTNode(data)
        elif data < self.data:
            if self.left:
                self.left.insert(data)
                return
            self.left = BSTNode(data)
        else:
            if self.right:
                self.right.insert(data)
                return
            self.right = BSTNode(data)

    def find_element(self, data):
        if not self.data:
            return False
        elif self.data == data:
            return True
        elif data < self.data:
            if self.left is None:
                return False
            return self.left.find_element(data)
        else:
            if self.right is None:
                return False
            return self.right.find_element(data)

    def delete(self, data):
        if self is None:
            return self

        # Deciding which branch has element to delete
        if data < self.data:
            self.left = self.left.delete(data)
            return self
        elif data > self.data:
            self.right = self.right.delete(data)
            return self

        # Deleted element is has one child empty
        if self.right is None:
            return self.left
        if self.left is None:
            return self.right

        # Deleted element has both children
        # Get the inorder successor (smallest in right child)
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.data = min_larger_node.data
        self.right.delete(min_larger_node.data)
        return self

    def pre_order(self):
        if not self.data:
            return
        print(self.data, end=' ')

        self.left.pre_order()
        self.right.pre_order()

