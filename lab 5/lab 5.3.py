n = int(input("Введите количество элементов: "))

numbers = []

for i in range(n):
    num = int(input(f"Введите элемент {i+1}: "))
    numbers.append(num)

positive_count = 0
negative_count = 0
even_count = 0

for num in numbers:
  
    if num > 0:
        positive_count += 1

   
    if num < 0:
        negative_count += 1

 
    if num % 2 == 0:
        even_count += 1

print("Массив:", numbers)
print("Количество положительных:", positive_count)
print("Количество отрицательных:", negative_count)
print("Количество чётных:", even_count)
