n = int(input("Введите количество элементов: "))

numbers = []

for i in range(n):
    num = int(input(f"Введите элемент {i+1}: "))
    numbers.append(num)

target = int(input("Введите число для поиска: "))

found = False

for i in range(n):
    if numbers[i] == target:
        print("Число найдено. Индекс:", i)
        found = True
        break   

if not found:
    print("Число в массиве не найдено.")
