def search_bst(n, key):
    if n is None or n.key == key:
        return n
    elif key < n.key:
        return search_bst(n.left, key)
    else:
        return search_bst(n.right, key)

def search_bst_parent(n, key, parent=None):
    if n is None or n.key == key:
        return parent
    elif key < n.key:
        return search_bst_parent(n.left, key, n)
    else:
        return search_bst_parent(n.right, key, n)

def find_min(node):
    while node.left is not None:
        node = node.left
    return node

def find_max(node):
    while node.right is not None:
        node = node.right
    return node
