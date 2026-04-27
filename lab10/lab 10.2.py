def create_tree():
    root = Node(20)

    root.left = Node(10)
    root.right = Node(30)

    root.left.left = Node(5)
    root.left.right = Node(15)

    root.right.left = Node(25)
    root.right.right = Node(35)

    return root