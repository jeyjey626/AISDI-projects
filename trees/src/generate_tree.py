from lxml import etree
import lxml.builder
from AVL import test_avl_tree
import queue


def generate_tree(first_elem):
    root = etree.Element("root")
    root.text = str(first_elem.data)
    q = queue.Queue()
    parent = root
    q.put([parent, first_elem])

    while not q.empty():
        parent, curr_node = q.get()
        if curr_node:
            if curr_node.left is not None:
                child_left = etree.SubElement(parent, "left_child")
                child_left.text = str(curr_node.left.data)
                q.put([child_left, curr_node.left])

            if curr_node.right is not None:
                child_right = etree.SubElement(root, "right_child")
                child_right.text = str(curr_node.right.data)
                q.put([child_right, curr_node.right])

    tree = etree.ElementTree(root)
    tree.write('AVL_Tree.xml', pretty_print=True)


if __name__ == '__main__':
    root = test_avl_tree()
    generate_tree(root)