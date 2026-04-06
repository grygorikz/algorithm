size = 5
hash_table = [[] for _ in range(size)]

def insert(key):
    index = key % size
    hash_table[index].append(key)

numbers = [10, 15, 20, 25, 30, 7]

for num in numbers:
    insert(num)

print(hash_table)