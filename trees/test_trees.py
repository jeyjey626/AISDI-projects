from unittest import TestCase
from src import BST


class TestTrees(TestCase):

    # testing BST tree
    def test_create(self):
        bst = BST.BSTNode(5)
        self.assertEqual(5, bst.data)

    def test_insert(self):
        bst = BST.BSTNode(5)
        bst.insert(1)
        self.assertEqual(1, bst.left.data)

    def test_insert_deeper(self):
        bst = BST.BSTNode(5)
        bst.insert(3)
        bst.insert(1)
        self.assertEqual(1, bst.left.left.data)

    def test_find_element_true(self):
        bst = BST.BSTNode(5)
        bst.insert(10)
        bst.insert(15)
        bst.insert(20)
        self.assertEqual(True, bst.find_element(20))

    def test_find_element_false(self):
        bst = BST.BSTNode(5)
        bst.insert(7)
        self.assertEqual(False, bst.find_element(20))

    def test_delete_no_children(self):
        bst = BST.BSTNode(5)
        bst.insert(10)
        bst.delete(10)
        self.assertEqual(None, bst.right)

    def test_delete_one_child_1(self):
        bst = BST.BSTNode(20)
        bst.insert(10)
        bst.insert(5)
        bst.delete(10)
        self.assertEqual(5, bst.left.data)

    def test_delete_one_child_2(self):
        bst = BST.BSTNode(20)
        bst.insert(25)
        bst.insert(26)
        bst.delete(25)
        self.assertEqual(26, bst.right.data)

    def test_delete_both_children(self):
        bst = BST.BSTNode(20)
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.delete(10)
        self.assertEqual(15, bst.left.data)
