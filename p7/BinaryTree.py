class BSTNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def count_node(n):
    if n is None:
        return 0
    return 1 + count_node(n.left) + count_node(n.right)

def count_leaf(n):
    if n is None:
        return 0
    if n.left is None and n.right is None:
        return 1
    return count_leaf(n.left) + count_leaf(n.right)

def calc_height(n):
    if n is None:
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    return max(hLeft, hRight) + 1
