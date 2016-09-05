class Tree:
    def __init__(self, key, parent_key):
        self.key = key
        self.parent_key = parent_key
        self.parent = False
        if parent_key == -1:
            self.parent = True



def preorder_traversal(tree):
    if tree.leaf:
        return
    print(tree.key)
    preorder_traversal(tree)
