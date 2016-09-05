# python3

import sys
import threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class Node:
    def __init__(self, key, parent_key):
        self.parent = False
        self.key = key
        self.parent_key = parent_key
        self.childrens = []
        self.leaf = True
        if(parent_key == -1):
            self.parent = not self.parent
            self.leaf = not self.leaf

    def add_child(self, child_key):
        self.childrens.append(child_key)
        self.leaf = not self.leaf


class Tree:
    def __init__(self, data):
        self.root = None
        self.max_height = 0
        self.node_pool = []
        self.make_node(data)
        self.make_tree()

    def make_node(self, data):
        for node_key, parent_key in enumerate(data):
            self.node_pool.append(Node(node_key, parent_key))

    def make_tree(self):
        for node_key, node in enumerate(self.node_pool):
            if node.parent:
                self.root = node
            parent_node = self.node_pool[node.parent_key]
            parent_node.add_child(node.key)

    def is_parent(self, node):
        if not node.parent:
            parent_node = self.node_pool[node.parent_key]
            max_height += 1

    def compute_height(self):
        height = 0
        for node in self.node_pool:
            if node.leaf:
                if(is_parent()):

        self.max_height = max(self.max_height, height)




def main():
    int_list =[1, 2, -1, 1, 8, 1, 5, 5, 2, 8, 8]
    tree = Tree(int_list)
    # print(tree.compute_height())

threading.Thread(target=main).start()
