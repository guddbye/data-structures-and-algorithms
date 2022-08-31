from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import Hashtable

def tree_intersection(tree_a, tree_b):
    table = Hashtable()
    matches = []

    def walk(root, run):
        if root is None:
            return
        run(root)
        walk(root.left, run)
        walk(root.right, run)

    def add_to_hashtable(root):
        table.set(str(root.value), root.value)

    def add_matches(root):
        if table.contains(str(root.value)) and root.value not in matches:
            matches.append(root.value)

    walk(tree_a.root, add_to_hashtable)
    walk(tree_b.root, add_matches)

    return matches
