linked_list = LinkedList()

for i in range(5):
    num = int(input(f"Введите число {i+1}: "))
    linked_list.add_to_end(num)

print("Ваш связный список:")
linked_list.print_list()