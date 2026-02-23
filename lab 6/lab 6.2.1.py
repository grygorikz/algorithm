#свой вариант
import random

n = int(input("Строки: "))
m = int(input("Столбцы: "))

# создаём массив
a = [[random.randint(1, 20) for _ in range(m)] for _ in range(n)]

print("\nМассив:")
for row in a:
    print(*row)

# сумма всех элементов
print("\nСумма всех элементов:", sum(sum(row) for row in a))

# максимальный элемент
print("Максимальный элемент:", max(max(row) for row in a))

# суммы строк и поиск максимальной
print("\nСуммы строк:")
max_sum = 0
max_row = 0

for i in range(n):
    s = sum(a[i])
    print(f"Строка {i+1}:", s)
    if s > max_sum:
        max_sum = s
        max_row = i + 1

# суммы столбцов
print("\nСуммы столбцов:")
for j in range(m):
    s = 0
    for i in range(n):
        s += a[i][j]
    print(f"Столбец {j+1}:", s)

print("\nСтрока с максимальной суммой:", max_row)