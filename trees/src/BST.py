# BST tree algorithm
import generate_tree
import numpy as np


class BSTNode:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if not self.data:
            return BSTNode(data)
        elif self.data == data:
            return self
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
            if self.left:
                self.left = self.left.delete(data)
            return self
        elif data > self.data:
            if self.right:
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


def print_to_xml(name, tree):
    generate_tree.generate_tree(name, tree)


def create_tree(elem_to_create):
    bst = BSTNode(elem_to_create[1])
    for elem in elem_to_create:
        bst.insert(elem)
    return bst


def search_tree(tree, elem_to_search):
    for elem in elem_to_search:
        tree.find_element(elem)


def delete_tree(tree, elem_to_delete):
    for elem in elem_to_delete:
        tree.delete(elem)
    return tree


if __name__ == '__main__':
    elements_to_insert = [np.random.randint(0, 100) for i in range(10)]
    bst_tree = create_tree(elements_to_insert)
    print_to_xml('xml/BST_Tree.xml', bst_tree)
