from lxml import etree
import numpy as np
import AVL
import queue


def generate_tree(name, first_elem):
    root = etree.Element("root")
    root.text = str(first_elem.data)
    q = queue.Queue()
    parent = root
    q.put([parent, first_elem])

    while not q.empty():
        parent, curr_node = q.get()
        if curr_node:
            print("Curr node data: {}".format(curr_node.data))
            if curr_node.left is not None:
                print("Curr left data: {}".format(curr_node.left.data))
                child_left = etree.SubElement(parent, "left_child")
                child_left.text = str(curr_node.left.data)
                q.put([child_left, curr_node.left])

            if curr_node.right is not None:
                print("Curr right data: {}".format(curr_node.right.data))
                child_right = etree.SubElement(parent, "right_child")
                child_right.text = str(curr_node.right.data)
                q.put([child_right, curr_node.right])

    tree = etree.ElementTree(root)
    tree.write(name, pretty_print=True)


if __name__ == '__main__':
    elements_to_insert = [i for i in range(10)]
    avl = AVL.AVLTree()
    root = AVL.create_tree(elements_to_insert)
    generate_tree('xml/AVL_Tree.xml', root)
