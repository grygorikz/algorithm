n = int(input("Введите количество элементов: "))

numbers = []

for i in range(n):
    num = int(input(f"Введите элемент {i+1}: "))
    numbers.append(num)

if n < 2:
    print("Ошибка: массив должен содержать минимум 2 элемента.")
else:
    
    max1 = numbers[0]
    max2 = numbers[0]

for num in numbers:
    if num > max1:
        max2=max1
        max1=num
    elif num > max2 and num != max1:
        max2 = num
    
    if max1 == max2:
        print("Второй по величине элемент отсутствует (все элементы равны).")
    else:
        print("второй по величине элемент:", max2)