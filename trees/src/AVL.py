# AVL tree algorithm
import numpy as np

class AVLNode:

    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data
        self.height = 1


class AVLTree(object):

    def insert(self, root, data):
        if not root:
            return AVLNode(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        # Height update
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Check balance
        balance = self.check_balance(root)

        # Unbalanced -> RR
        if balance < -1 and data > root.right.data:
            return self.rotate_left(root)

        # Unbalanced -> LL
        if balance > 1 and data < root.left.data:
            return self.rotate_right(root)

        # Unbalanced -> RL
        if balance < -1 and data < root.right.data:
            if root.right.left:
                root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        # Unbalanced -> LR
        if balance > 1 and data > root.left.data:
            if root.left.right:
                root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        return root

    def find_element(self, root, data):
        if not root:
            return False

        if root.data == data:
            return True

        elif data < root.data:
            return self.find_element(root.left, data)
        else:
            return self.find_element(root.right, data)

    def delete(self, root, data):
        if not root:
            return root

        if data < root.data:
            root.left = self.delete(root.left, data)
            return root
        elif data > root.data:
            root.right = self.delete(root.right, data)
            return root

        # if root is leaf
        if root.left is None and root.right is None:
            return None

        # if root has one empty children
        if root.left is None:
            tmp = root.right
            root = tmp
            return tmp
        elif root.right is None:
            tmp = root.left
            root = None
            return tmp

        # if both children exist
        parent = root
        child = root.right

        while child.left:
            parent = child
            child = child.left

        if parent != root:
            parent.left = child.right
        else:
            parent.right = child.right

        root.data = child.data

        # Height update
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Check balance
        balance = self.check_balance(root)

        # Unbalanced -> RR
        if balance < -1 and self.check_balance(root.right) <= 0:
            return self.rotate_left(root)

        # Unbalanced -> LL
        if balance > 1 and self.check_balance(root.left) >= 0:
            return self.rotate_right(root)

        # Unbalanced -> RL
        if balance < -1 and self.check_balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        # Unbalanced -> LR
        if balance > 1 and self.check_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        return root

    def pre_order(self, root, list =[]):
        if not root:
            return
        list.append(root.data)
        self.pre_order(root.left, list)
        self.pre_order(root.right, list)
        return list

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def check_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def rotate_right(self, z):
        y = z.left
        right_subtree = y.right

        # Rotation
        y.right = z
        z.left = right_subtree

        # Height update
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Root after right rotation
        return y

    def rotate_left(self, z):
        y = z.right
        left_subtree = y.left

        # Rotation
        y.left = z
        z.right = left_subtree

        # Height update
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Root after left rotation
        return y


def create_tree(elements_to_insert):
    avl = AVLTree()
    root = None

    for i in elements_to_insert:
        root = avl.insert(root, i)
    return root


def search_tree(root, elements_to_search):
    avl = AVLTree()
    for i in elements_to_search:
        avl.find_element(root, i)


def delete_tree(root, elements_to_delete):
    avl = AVLTree()
    for i in elements_to_delete:
        root = avl.delete(root, i)
    return root


if __name__ == '__main__':
    elements_to_insert = [np.random.randint(0, 100) for i in range(10)]
    root = create_tree(elements_to_insert)
    print(root.data)
