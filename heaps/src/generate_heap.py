from lxml import etree
from n_heap import NHeap
import queue


def generate_heap(heap, n):
    root = etree.Element("root")
    root.text = str(heap.heap_list[0])
    q = queue.Queue()
    parent = root
    q.put([parent, heap.heap_list[0], 0])

    while not q.empty():
        parent, curr_node, index = q.get()
        children = heap.get_children(index)
        i = 0
        for child in children:
            child_node = etree.SubElement(parent, "child")
            child_node.text = str(child)
            q.put([child_node, child, index * n + 1 + i])
            i += 1

    tree = etree.ElementTree(root)
    tree.write('/src/xml/' + str(n)+'_heap.xml', pretty_print=True)


if __name__ == '__main__':
    n = 2
    bin_heap = NHeap(n)
    for i in range(20):
        bin_heap.insert(i)
    generate_heap(bin_heap, n)