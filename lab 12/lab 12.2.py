numbers = [5, 2, 5, 3, 2, 5]
count_dict = {}

for num in numbers:
    count_dict[num] = count_dict.get(num, 0) + 1

print(count_dict)