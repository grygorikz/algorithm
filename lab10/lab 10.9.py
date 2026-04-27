def search(node, value):
    if node is None:
        return False
    if node.value == value:
        return True
    return search(node.left, value) or search(node.right, value)
