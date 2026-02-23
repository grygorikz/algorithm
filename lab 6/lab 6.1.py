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

print("\nSumma elementov:", total)
print("Maksimalnyi element:", maximum)
