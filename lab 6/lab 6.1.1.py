#свой вариант
import random

# Ввод размеров
n = int(input("Строки: "))
m = int(input("Столбцы: "))

# Создание массива
matrix = [[random.randint(1, 20) for j in range(m)] for i in range(n)]

# Вывод таблицы
print("\nМассив:")
for row in matrix:
    print(*row)

# Сумма и максимум
total = sum(sum(row) for row in matrix)
maximum = max(max(row) for row in matrix)

print("\nСумма:", total)
print("Максимальный элемент:", maximum)