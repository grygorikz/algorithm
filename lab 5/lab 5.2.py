n = int(input("Введите количество элементов: "))

numbers = []

for i in range(n):
    num = int(input(f"Введите элемент {i+1}: "))
    numbers.append(num)

total = 0
for num in numbers:
    total += num

maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num

minimum = numbers[0]
for num in numbers:
    if num < minimum:
        minimum = num

average = total / n

print("Массив:", numbers)
print("Сумма:", total)
print("Максимальный элемент:", maximum)
print("Минимальный элемент:", minimum)
print("Среднее арифметическое:", average)
