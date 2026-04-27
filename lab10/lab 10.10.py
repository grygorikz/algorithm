root = create_tree()

print("Корень:", root.value)
print("Левый потомок корня:", root.left.value)
print("Правый потомок корня:", root.right.value)

print("\nPreorder:")
preorder(root)

print("\nInorder:")
inorder(root)

print("\nPostorder:")
postorder(root)

print("\n\nКоличество узлов:", count_nodes(root))
print("Количество листьев:", count_leaves(root))
print("Высота дерева:", tree_height(root))

print("\nПоиск 15:", search(root, 15))
print("Поиск 100:", search(root, 100))