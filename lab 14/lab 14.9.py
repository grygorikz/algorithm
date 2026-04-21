nums = [1, 2, 3, 4, 5]

even = []
odd = []

for num in nums:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Четные:", even)
print("Нечетные:", odd)