import random

rows = int(input("vvedite kolichestvo strok: "))
cols = int(input("vvedite kolichestvo stolbcov "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(random.randint(0, 50))
    matrix.append(row)

print("\nMatrica")
for row in matrix:
    for value in row:
        print(f"{value:4}", end="")
    print()

# Сумма элементов
total = 0
maximum = matrix[0][0]

for row in matrix:
    for value in row:
        total += value
        if value > maximum:
            maximum = value

row_sums = []

for i in range(rows):
    row_sum = sum(matrix[i])
    row_sums.append(row_sum)
    print(f"Сумма строки {i}: {row_sum}")

# Сумма по столбцам
for j in range(cols):
    col_sum = 0
    for i in range(rows):
        col_sum += matrix[i][j]
    print(f"Сумма столбца {j}: {col_sum}")

# Поиск строки с максимальной суммой
max_row_index = row_sums.index(max(row_sums))
print("Строка с максимальной суммой:", max_row_index)


print("\nSumma elementov:", total)
print("Maksimalnyi element:", maximum)